"""DoSites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.views.static import serve
from DoSites import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', include('about.urls')),  # 公司简介
    path('news/', include('news.urls')),    # 新闻动态
    path('products/', include('products.urls')),  # 产品中心
    path('service/', include('service.urls')),    # 服务支持
    path('science/', include('science.urls')),    # 科研基地
    path('contact/', include('contact.urls')),    # 人才招聘
    path('api/', include('institution.urls')),  # 机构信息-API
    # path('institution-admin/', institution_admin_site.urls),
    # path('api/institution1/', institution_list),
    # path('ueditor/', include('DjangoUeditor.urls')),   # 编辑
    # path('search/', include('haystack.urls')),    # 添加haystack搜索的路径
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 后面的加了图片及文件才可以访问


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('science/', include('science.urls')),
#     path('about/', include('about.urls')),  # , namespace='about'
# ] + serve(r'^/(?P<path>.*)$', settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
