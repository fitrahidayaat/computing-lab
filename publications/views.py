from django.shortcuts import render
from publications.models import Publication

# Create your views here.

def publicationsView(req):
    publications = Publication.objects.all()
    ctx = {
        'title': 'Computing Laboratory - Publications',
        'publications': publications
    }
    return render(req, 'publications/publications.html', ctx)
