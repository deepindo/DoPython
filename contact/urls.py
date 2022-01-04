from django.urls import path
from contact import views


app_name = 'contact'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('recruit/', views.recruit, name='recruit'),
]