from django.urls import path
from products import views


app_name = 'products'
urlpatterns = [
    path('productList/<str:productName>/', views.productList, name='productList'),
    path('productDetail/<int:id>/', views.productDetail, name='productDetail'),
]