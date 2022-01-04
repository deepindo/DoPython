from django.urls import path
from science import views


app_name = 'science'
urlpatterns = [
    path('science', views.science, name='science'),
]