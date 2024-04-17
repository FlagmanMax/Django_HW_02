from django.urls import path
from . import views
urlpatterns = [
    path('', views.seminar2, name='seminar2'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('statistic/', views.statistic, name='statistic'),
    path('authors/', views.authors_read, name='authors'),
    path('articles/', views.articles_read, name='articles'),
    path('articles_by_author/', views.articles_by_author, name='articles_by_author'),


]
