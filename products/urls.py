from django.urls import path

from . import views
from products.solver import answer
from products.solver4 import jawaban
from products.solver16 import hasil
from products.solver_yin_yang import answer as answerYinYang

urlpatterns = [
    path('', views.productsView, name='products'),
    path('products4/', views.products4View, name='products4'),
    path('products16/', views.products16View, name='products16'),
    path('products16/', views.products16View, name='products16'),
    path('yin-yang/', views.yinYangView, name='yin_yang'),
    path('answer/', answer, name='answer'),
    path('answer4/', jawaban, name='jawaban'),
    path('answer16/', hasil, name='hasil'),
    path('answer-yin-yang/', answerYinYang, name='answer_yin_yang'),
]
