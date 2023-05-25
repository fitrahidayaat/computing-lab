from django.shortcuts import render
from laboratory.models import Topic

# Create your views here.
def landingView(req):
    ctx = {
        'title': 'Computing Laboratory',
        'advance': Topic.objects.filter(study='advance', status='active'),
        'basic': Topic.objects.filter(study='basic', status='active')
    }
    return render(req, 'landing/landing.html', ctx)