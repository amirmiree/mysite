from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_home(request):
    return HttpResponse("<h1>Home Page</h1>")

def index_contact(request):
    return HttpResponse("<h1>Contact Page")


def index_about(request):
    return HttpResponse("<h1>About Page</h1>")