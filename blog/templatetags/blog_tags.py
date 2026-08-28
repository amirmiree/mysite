from django import template
from  blog.models import Post
register = template.Library()


@register.simple_tag
def hello():
    return 'hello'

@register.simple_tag
def calculate(a,b):
    return a*b

@register.simple_tag
def default(f=5):
    return f

@register.simple_tag
def postcount(name= "published_count"):
    posts = Post.objects.filter(status =1).count()
    return posts


@register.simple_tag
def showpublished(name= "published_post"):
    posts = Post.objects.filter(status =1)
    return posts


@register.filter
def filetrcontent(value, arg):
    return value[:arg]



@register.inclusion_tag('popularpost.html')
def popularpost():
    # posts= Post.objects.filter(status=1).order_by("created_date")
    posts= Post.objects.filter(status=1).order_by("-created_date")[:1]
    return {"posts": posts}