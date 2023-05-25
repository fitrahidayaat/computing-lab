from django.urls import path

from . import views

urlpatterns = [
    path('', views.recruitmentView, name='recruitment'),
    path('submit', views.submitView),
    #path('check', views.checkView),
]
