from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_html(request):
    return render(request ,"website/index.html" )

def index_contact(request):
    return render(request , "website/contact.html")


def index_about(request):
    return render(request , "website/about.html")