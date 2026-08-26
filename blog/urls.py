from django.contrib import admin
from django.urls import path
from blog.views import *
app_name = "website"
app_name = "blog"
urlpatterns = [
    path("",index_blog_html , name='blog'),
    path("<int:pid>", index_blog_single, name = 'single-blog'),
]