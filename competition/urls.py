from django.urls import path

from . import views

urlpatterns = [
    # path('ccp2020-elimination-unfreeze', views.ccp2020_scoreboard_elimination_unfreeze),
    # path('ccp2021-warmingup-unfreeze', views.ccp2021_scoreboard_warmingup_unfreeze),
    # path('ccp2021-elimination-public', views.ccp2021_scoreboard_elimination_public),
    # path('ccp2021-elimination-jury', views.ccp2021_scoreboard_elimination_jury),
    # path('ccp2021-elimination-unfreeze', views.ccp2021_scoreboard_elimination_unfreeze),
    # path('ccp2021-final-unfreeze', views.ccp2021_scoreboard_final_unfreeze),
    path('ccp2018-final-jury', views.ccp2018_scoreboard_final_jury),
    # path('ccp2021-final-public', views.ccp2021_scoreboard_final_public),
    path('ccp2021-final-jury', views.ccp2021_scoreboard_final_jury),
    path('impact2022-penyisihan', views.impact2022_scoreboard_penyisihan),
    path('impact2022-final', views.impact2022_scoreboard_final),
]
