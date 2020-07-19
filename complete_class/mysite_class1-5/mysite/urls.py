"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from article.views import article_detail,article_list

urlpatterns = [
    path('admin/', admin.site.urls),#后台管理网址
    path('', views.index),   #设置一个空的路由，不设置就是ip后没有目录，需要创建一个方法
    path('article/', include('article.urls')), #使用include引用app中的urls.py
]
