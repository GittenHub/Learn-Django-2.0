from django.contrib import admin
from django.urls import include,path
#from blog.views import blog_list
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login_for_modal/', views.login_for_modal, name='login_for_modal'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name='user_info'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
]