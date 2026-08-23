from django.db import models
# data base --> create table the name is : app_name-class-name --> coulns --> filds
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()