from django.urls import path
from about import views


app_name = 'about'
urlpatterns = [
    path('survey/', views.survey, name='survey'),  # 路由访问的路径，name为反向解析时用到
    path('honor/', views.honor, name='honor'),  # 路由访问的路径，name为反向解析时用到
]