from django.shortcuts import render

# Create your views here.
def index_blog_html(request):
    return render(request  ,"blog/blog-home.html" )

def index_blog_single(request):
    return render(request ,"blog/blog-single.html" )