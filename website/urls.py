from django.contrib import admin
from django.urls import path
from website.views import *
urlpatterns = [
    path("",index_html),
    path("contact/", index_contact),
    path("about/", index_about)

]