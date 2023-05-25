import requests
import json

def read(file):
    f = open(file, 'r')
    content = f.read()
    f.close()
    return content

tc = [
    {
        'in': read('recruitment/tc/1.in'),
        'ans': read('recruitment/tc/1.ans'),
        'time': 0.01 * 5
    },
    {
        'in': read('recruitment/tc/2.in'),
        'ans': read('recruitment/tc/2.ans'),
        'time': 0.01 * 5
    }
]

def jdoodle(nim, solution):

    try:
        for i in tc:
            params = {
                'clientId': 'f4bfd3ca6b8d76745b26336c89c4f35d',
                'clientSecret': '295e6defd36d3591c36da01020b6f0be99957db7cc24de785c24e668832a2ae1',
                'stdin': i['in'],
                'language': 'python3',
                'script': solution,
                'versionIndex': 3
            }
        
            res = requests.post('https://api.jdoodle.com/v1/execute', json=params).json()
            print(nim, res)
            if 'error' in res:
                return 'ERROR'
            
            if 'Timeout' in res['output']:
                return "TIME_LIMIT_EXCEEDED"

            if float(res['cpuTime']) > i['time']:
                return 'TIME_LIMIT_EXCEEDED'

            if res['output'].rstrip() != i['ans'].rstrip():
                return 'WRONG_ANSWER'

        if nim not in LULUS:
            return 'REJECTED'
    except Exception as e:
        print(e)
        return 'INTERNAL_ERROR'
    return 'ACCEPTED'

def submit(nim, solution):
    datas = []
    i = 0
    while i < len(tc):
        params = {
            'input': tc[i]['in'],
            'lang': 'Python3',
            'code': solution,
            'save': False
        }
       
        res = requests.post('https://ide.geeksforgeeks.org/main.php', data=params).json()
        if res['status'] == 'SUCCESS':
            datas.append({
                'tc': i,
                'id': res['sid']
            })

            i += 1
        else:
            print('Error gaes pas submit', res)
    
    return json.dumps(datas)

def check(nim, datas):
    try:
        datas = json.loads(datas)
        for i in datas:
            t = tc[i['tc']]
            fetch = requests.post('https://ide.geeksforgeeks.org/submissionResult.php', data={'sid': i['id'], 'requestType': 'fetchResults'}).json()
            if fetch['status'] != 'IN-QUEUE':
                if 'rntError' in fetch:
                    if (float(fetch['time']) > t['time']) or (fetch['rntError'] == 'Time Limit Exceeded\n'):
                        return 'TIME_LIMIT_EXCEEDED'
                    return 'ERROR'
                if fetch['output'].rstrip() != t['ans'].rstrip():
                    return 'WRONG_ANSWER'
            else:
                return 'IN_QUEUE'

        if nim not in LULUS:
            return 'REJECTED'
    except Exception as e:
        print(e)
        return 'INTERNAL ERROR'

    return 'ACCEPTED'

LULUS = {
    '1301180405',
    '1301201431',
    '1301194081',
    '1301190369',
    '1301204253',
    '1301194018',
    '1301194220',
    '1301194102',
    '1301194152',
    '6706201135',
    '1302202072',
    '1303202006',
    '1301204337',
    '1303194073',
    '1301204096',
    '1301204090',
    '1301190371',
    '1301190230',
    '1301204068',
    '1301204097',
    '1301200345',
    '1301204447',
    '1301204114',
    '1301204083',
    '1301201154',
    '1301204316',
    '1301194376',
    '1301190392',
    '1301180154'
}