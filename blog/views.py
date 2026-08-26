from django.shortcuts import render ,get_object_or_404
from blog.models import Post
from datetime import date
# Create your views here.
def index_blog_html(request):
    posts = Post.objects.filter(status =1)
    context = {"posts": posts}
    return render(request  ,"blog/blog-home.html", context )

def index_blog_single(request, pid):
    posts_ac = Post.objects.filter(status =1)
    post = get_object_or_404(posts_ac,id= pid)
    context = {"post": post}
    return render(request ,"blog/blog-single.html", context )

def test(request):
    # get data from databse 
    posts_data = Post.objects.all()
    posts = []

    for post in posts_data:
        now = date.today()

        if post.published_date > now:
            posts.append(post)

    context = {"posts": posts}
    return render(request ,"test.html", context )

