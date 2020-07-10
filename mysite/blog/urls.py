from django.urls import path
from . import views

#http：localhost:8000/blog/1
#http：localhost:8000/

#start with blog
urlpatterns = [
    #http：localhost:8000/blog/1
    path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
]
