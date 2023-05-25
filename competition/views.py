from django.shortcuts import render
from . import ccp2020_participants
from . import ccp2021_participants
from . import ccp2018_participants
from . import impact2022_participants
from . import hackerrank_scoreboard_generator
import os
import time

template_path = os.path.join('competition', 'templates', 'competition')

def generate_scoreboard(hr_slug, sb_filename, ts_filename, participants, freeze=-1):
    with open(os.path.join(template_path, sb_filename), 'w+') as sb_file:
        sb_content = hackerrank_scoreboard_generator.render(hr_slug, participants, freeze)
        sb_file.write(sb_content)

    with open(os.path.join(template_path, ts_filename), 'w+') as ts_file:
        ts_file.write(str(int(time.time())))

def get_scoreboard(hr_slug, participants, freeze=-1):
    freeze_status = 'freeze' if freeze != -1 else 'unfreeze'
    sb_filename = f'{hr_slug}-{freeze_status}.html'
    ts_filename = f'{hr_slug}-{freeze_status}-ts'
    if os.path.exists(os.path.join(template_path, sb_filename)) and os.path.exists(os.path.join(template_path, ts_filename)):
        with open(os.path.join(template_path, ts_filename), 'r') as ts_file:
            ts = ts_file.read()
            ts = int(ts)
            if int(time.time()) - int(ts) > 1 * 30:
                print('Generating new scoreboard...')
                generate_scoreboard(hr_slug, sb_filename, ts_filename, participants, freeze)
    else:
        print('Generating scoreboard...')
        generate_scoreboard(hr_slug, sb_filename, ts_filename, participants, freeze)

    return sb_filename

# def ccp2020_scoreboard_final_unfreeze(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2020-final',
#         freeze=False,
#         participants = ccp2020_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')

# def ccp2021_scoreboard_warmingup_unfreeze(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2021-warming-up',
#         freeze=-1,
#         participants = ccp2021_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')

# def ccp2021_scoreboard_elimination_unfreeze(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2021-elimination',
#         freeze=-1,
#         participants = ccp2021_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')

# def ccp2021_scoreboard_elimination_public(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2021-elimination',
#         freeze=1638079200,
#         participants = ccp2021_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')

# def ccp2021_scoreboard_elimination_jury(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2021-elimination',
#         freeze=-1,
#         participants = ccp2021_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')

# def ccp2021_scoreboard_elimination_unfreeze(req):
#     return render(req, 'competition/ccp2021-elimination-unfreeze.html')

# def ccp2021_scoreboard_final_unfreeze(req):
#     return render(req, 'competition/ccp2021-final-unfreeze.html')
    
# def ccp2021_scoreboard_final_public(req):
#     sb_filename = get_scoreboard(
#         hr_slug='computing-competitive-programming-2021-final-1g36xkl',
#         freeze=1638678600,
#         participants = ccp2021_participants.get_participants()
#     )

#     return render(req, f'competition/{sb_filename}')


def ccp2021_scoreboard_final_jury(req):
    sb_filename = get_scoreboard(
        hr_slug='computing-competitive-programming-2021-final-1g36xkl',
        freeze=-1,
        participants = ccp2021_participants.get_participants()
    )

    return render(req, f'competition/{sb_filename}')

def ccp2018_scoreboard_final_jury(req):
    sb_filename = get_scoreboard(
        hr_slug='computing-competitive-programming-2018-final',
        freeze=-1,
        participants = ccp2018_participants.get_participants()
    )

    return render(req, f'competition/{sb_filename}')

def impact2022_scoreboard_penyisihan(req):
    sb_filename = get_scoreboard(
        hr_slug='impact-2022-penyisihan',
        freeze=-1,
        participants = impact2022_participants.get_participants()
    )

    return render(req, f'competition/{sb_filename}')

def impact2022_scoreboard_final(req):
    sb_filename = get_scoreboard(
        hr_slug='impact-2022-final',
        freeze=-1,
        participants = impact2022_participants.get_participants()
    )

    return render(req, f'competition/{sb_filename}')