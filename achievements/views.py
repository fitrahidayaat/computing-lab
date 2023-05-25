from django.shortcuts import render

def achievementsView(req):
    ctx = {
        'title': 'Computing Laboratory - Achievements'
    }
    return render(req, 'achievements/achievements.html', ctx)