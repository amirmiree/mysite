from django.contrib import admin
from django.urls import path
from website.views import *
urlpatterns = [
    path("home/",index_home),
    path("contact/", index_contact),
    path("about/", index_about)

]