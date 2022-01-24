from django.urls import path
from institution import views

app_name = 'institution'
urlpatterns = [
    path('institution_list/', views.institution_list),
    path('institution_add/', views.institution_add),
]