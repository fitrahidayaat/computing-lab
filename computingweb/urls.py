"""computingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve

from landing.views import landingView
from achievements.views import achievementsView
from publications.views import publicationsView
from recruitment.views import recruitmentView
from laboratory.views import laboratoryView

from products import urls as products_url

from recruitment import urls as recruitment_url

from competition import urls as competition_url

from . import views


urlpatterns = [
    path('admin/', admin.site.urls), #Done
    path('', landingView, name=''), #Done
    path('achievements/', achievementsView, name='achievements'), #DONE
    path('laboratory/', laboratoryView, name='laboratory'), #DONE
    path('products/', include(products_url)), #DONE
    path('publications/', publicationsView, name='publications'), #DONE
    path('recruitment/', include(recruitment_url)), #DONE
    path('competition/', include(competition_url)),
    re_path(r'^.well-known/acme-challenge/.*$', views.acme_challenge, name='acme-challenge'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
