from copy import deepcopy
from jinja2 import Template
from datetime import datetime
import time
import requests
import string
import os
import pytz
import json

def get_contest_data(slug, username, password):
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.10',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    auth = (username, password)

    params = {
        '_': time.time()
    }

    data = requests.get(f'https://www.hackerrank.com/rest/contests/{slug}', params=params, auth=auth, headers=headers).json()
    return data

def get_hr_problem_data(slug, username, password, offset, limit):
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.10',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    auth = (username, password)

    params = {
        'offset': offset,
        'limit': limit,
        '_': time.time()
    }

    data = requests.get(f'https://www.hackerrank.com/rest/contests/{slug}/challenges', params=params, auth=auth, headers=headers).json()
    return data

def get_hr_submission_data(slug, username, password, offset, limit):
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.10',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    auth = (username, password)

    params = {
        'offset': offset,
        'limit': limit,
        '_': time.time()
    }

    data = requests.get(f'https://www.hackerrank.com/rest/contests/{slug}/judge_submissions', params=params, auth=auth, headers=headers).json()
    return data

def render(contest_slug, participants, freeze=-1):
    hr_contest_data = get_contest_data(contest_slug, 'ccp2021', 'ccp2021')
    hr_problem_data = get_hr_problem_data(contest_slug, 'ccp2021', 'ccp2021', 0, 10000)
    hr_submission_data = get_hr_submission_data(contest_slug, 'ccp2021', 'ccp2021', 0, 10000)

    problems = dict()

    for i in zip( string.ascii_uppercase, hr_problem_data['models']):
        code = i[0]
        p = i[1]
        problems[p['slug']] = {
            'code': code,
            'name': p['name'],
            'slug': p['slug'],
            'file': f'/static/competition/problem/{contest_slug}/{code}.pdf',
            'first_solver': None,
            'r_first_solver': '-',
            'count_of_solver': 0,
            'r_count_of_solver': '0 of 0 (0%)',
            'count_of_submission': 0, # including post ac? i think no'
            'r_success_rate': '0%',
        }

    skeleton = {
        'fullname': '-',
        'major': '-',
        'class': '-',
        'total_problem': 0,
        'total_score': 0,
        'total_time': 0,
    }

    for p in problems:
        skeleton[problems[p]['slug']] = {
            'status': '?',
            'penalty': 0,
            'time': 0,
            'attempt': 0,
            'max_score': 0,
            'max_score_time': 0,
            'max_score_penalty': 0,
        }

    CONTESTANT = dict()
    
    # inserttime itu created_at + penalty
    for i in reversed(hr_submission_data['models']):
        # TODO : skip before contest and break after contest
        if not i['in_contest_bounds']:
            continue

        if i['hacker_username'] not in CONTESTANT:
            CONTESTANT[i['hacker_username']] = deepcopy(skeleton)
                
        hacker = CONTESTANT[i['hacker_username']]
        p = i['challenge']['slug']
        
        if hacker[p]['status'] != 'Accepted':
            if freeze != -1 and i['created_at'] > freeze:
                hacker[p]['status'] = 'Pending'
            else:
                hacker[p]['status'] = i['status']
                hacker[p]['attempt'] += 1

                if i['status'] == 'Accepted':
                    hacker['total_problem'] += 1
                    problems[p]['count_of_solver'] += 1
                    
                    if problems[p]['first_solver'] == None:
                        problems[p]['first_solver'] = i['hacker_username']
                else:
                    if hr_contest_data['model']['leaderboard_format'] == 'acm':
                        # comment the line below to ignore penalty
                        hacker[p]['penalty'] = 0
                        # hacker[p]['penalty'] += (hr_contest_data['model']['penalty'] // 60)
                        # hacker[p]['penalty'] += (1200 // 60)

                if i['score'] > hacker[p]['max_score']:
                    hacker['total_score'] -= hacker[p]['max_score']
                    hacker['total_score'] +=  i['score']
                    
                    hacker['total_time'] -=  hacker[p]['max_score_time'] + hacker[p]['max_score_penalty']
                    hacker['total_time'] += i['time_from_start'] + hacker[p]['penalty']

                    hacker[p]['max_score'] = i['score']
                    hacker[p]['max_score_time'] = i['time_from_start']
                    hacker[p]['max_score_penalty'] = hacker[p]['penalty']

                problems[p]['count_of_submission'] += 1

    # Registering participants
    for p in participants:
        try:
            CONTESTANT[p['hackerrank']]['fullname'] = p['name']
            CONTESTANT[p['hackerrank']]['class'] = p['class']
            CONTESTANT[p['hackerrank']]['major'] = p['major']
        except Exception:
            continue

    # Rendering problem data
    for p in problems:
        fs = problems[p]['first_solver']
        prob = problems[p]
        if fs:
            fs_hacker = CONTESTANT[fs]  
            prob['r_first_solver'] = '{} ({}:{:02d})'.format(fs_hacker['fullname'], int(fs_hacker[p]['max_score_time']), round((fs_hacker[p]['max_score_time'] % 1) * 60))

        solver_rate = 0.00 
        try:
            solver_rate = prob['count_of_solver'] / len(CONTESTANT) * 100
        except Exception:
            pass

        prob['r_count_of_solver'] = '{} of {} ({:.2f}%)'.format(prob['count_of_solver'], len(CONTESTANT), solver_rate)

        success_rate = 0.00 
        try:
            success_rate = prob['count_of_solver'] / prob['count_of_submission'] * 100
        except Exception:
            pass
        
        prob['r_success_rate'] = '{:.2f}%'.format(success_rate)
        
    # Rendering user data
    jinja_users = []
    sort_user_compare = lambda x: (-CONTESTANT[x]['total_score'], CONTESTANT[x]['total_time'])
    if hr_contest_data['model']['leaderboard_format'] == 'acm':
        sort_user_compare = lambda x: (-CONTESTANT[x]['total_problem'], CONTESTANT[x]['total_time'])

    for idx, username in enumerate(sorted(CONTESTANT, key=sort_user_compare)):
        hacker = CONTESTANT[username]

        user = {
            'rank': idx + 1 if hacker['total_score'] > 0 else '-',
            'fullname': hacker['fullname'],
            'hackerrank': username,
            'major': hacker['major'],
            'class': hacker['class'],
            'solved': hacker['total_problem'],
            'total_score': '{:.2f}'.format(hacker['total_score']),
            'total_time': '{}:{:02d}'.format(int(hacker['total_time']), round((hacker['total_time'] % 1) * 60)),
            'problems': dict()
        }
        
        for p in problems:
            status = []
            if hacker[p]['status'] == 'Accepted':
                status.append('ac')
            elif hacker[p]['status'] == 'Pending':
                status.append('pending')
            elif hacker[p]['status'] != '?':
                status.append('not-ac')
            
            if problems[p]['first_solver'] == username:
                status.append('fs')

            user['problems'][p] = {
                'slug': p,
                'attempt': '{} {}'.format(hacker[p]['attempt'], 'try' if hacker[p]['attempt'] == 1 else 'tries'),
                'max_score': '{:.2f}'.format(hacker[p]['max_score']),
                'max_score_time': '{}:{:02d}'.format(int(hacker[p]['max_score_time']), round((hacker[p]['max_score_time'] % 1) * 60)),
                'penalty': '+{:.2f}'.format(hacker[p]['penalty'] if hacker[p]['status'] == 'Accepted' else 0),
                'status': ' '.join(status),
            }
        jinja_users.append(user)

    rendered = None
    last_fetched = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%-d/%m/%Y, %H:%M:%S")

    scoreboard_html_template = 'hr-sb-template-ioi.html'
    if hr_contest_data['model']['leaderboard_format'] == 'acm':
        scoreboard_html_template = 'hr-sb-template-acm.html'
    with open(os.path.join(os.path.dirname(__file__), scoreboard_html_template)) as f:
        t = Template(f.read())
        rendered = t.render({
            'competition_name': hr_contest_data['model']['name'],
            'users': jinja_users,
            'problems': problems,
            'last_fetched': last_fetched,
            'last_fetched_epoch': int(time.time()),
        })

    return rendered