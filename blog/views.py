from django.shortcuts import render
from blog.models import Post
# Create your views here.
def index_blog_html(request):
    return render(request  ,"blog/blog-home.html" )

def index_blog_single(request):
    context = {"name": "amir", "lastname": "miri"}
    return render(request ,"blog/blog-single.html", context )

def test(request):
    # get data from databse 
    posts = Post.objects.all()
    context = {"post": posts}
    return render(request ,"test.html", context )