from django.contrib import admin
from django.urls import path
from website.views import *
app_name = "website"
urlpatterns = [
    path("",index_html , name= 'index'),
    path("contact/", index_contact, name = 'contact'),
    path("about/", index_about, name = 'about')

]