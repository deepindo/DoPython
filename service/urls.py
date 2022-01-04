from django.urls import path
from service import views


app_name = 'service'
urlpatterns = [
    path('download/', views.download, name='download'),  # 资料下载页面
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),  # 资料下载
    path('facedetect/', views.facedetect, name='facedetect'),  # 本地人脸检测api
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
    path('facedetectDemo/', views.facedetectDemo, name='facedetectDemo'),  # 网络api人脸检测
]