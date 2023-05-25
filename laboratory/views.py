from django.shortcuts import render
from laboratory.models import Topic, Member

def laboratoryView(req):
    heads = Member.objects.filter(role='head')
    ctx = {
        'title' : "Computing Laboratory - About Us",
        'topics' : Topic.objects.all(),
        'head' : heads[0] if heads else {},
        'assistants' : Member.objects.filter(role='assistant'),
        'members': Member.objects.all(),
        'generations': [
            {'id': "gen1", 'name': "1.0"},
            {'id': "gen2", 'name': "2.0"},
            {'id': "gen3", 'name': "3.0"},
            {'id': "gen4", 'name': "4.0"},
            {'id': "gen5", 'name': "5.0"},
            {'id': "gen6", 'name': "6.0"}
        ],
        'gen': "6.0",
    }
    return render(req, 'laboratory/laboratory.html', ctx)