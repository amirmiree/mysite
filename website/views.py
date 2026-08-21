from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_html(request):
    return render(request ,"index.html" )

def index_contact(request):
    return render(request , "contact.html")


def index_about(request):
    return render(request , "about.html")