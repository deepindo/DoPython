from django.urls import path
from news import views


app_name = 'news'
urlpatterns = [
    path('newsList/<str:news_name>/', views.newsList, name='newsList'),
    path('newsDetail/<int:id>/', views.newsDetail, name='newsDetail'),
]