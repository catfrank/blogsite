from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('writings/', views.writings, name='writings'),
    path('words/', views.words, name='words'),
    path('sentences/', views.sentences, name='sentences'),
]