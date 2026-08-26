from django.contrib import admin
from blog.models import Post
# Register your models here.


# there are  a lot of things to do

# first way way is create  class :
class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    # ability of editing and add new post based on thses options 
    # list is so useful to have quick look at data 
    list_display = ("title", "author","updated_date","created_date","published_date","status","content_viwe")
    # lets have a filter by an eleman:
    list_filter = ("status","author")
    # lets have ordering 
    # ordering  =("created_date",)
    # reverse
    # ordering = ("-created_date",)
    # search fields let you to search  words in wherever you select:
    search_fields = ("title", "content")
    # eleman vorodi bayad as no tme bashe! daste bande base on created date
admin.site.register(Post, Postadmin)


# second way:
# @admin.register(Post)
#class Postadmin(admin.ModelAdmin):
    # pass
