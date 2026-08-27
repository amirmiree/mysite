from django.db import models
from django.contrib.auth.models import User
# data base --> create table the name is : app_name-class-name --> coulns --> filds
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    # tag
    imgae = models.ImageField(upload_to='blog/', default ='blog/default.jpg')
    author = models.ForeignKey( User , on_delete=models.SET_NULL, null =True )
    category = models.ManyToManyField(Category)
    content_viwe = models.IntegerField(default = 0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null = True)
    created_date= models.DateField(auto_now_add= True)
    updated_date= models.DateField(auto_now=True)
    
    # in the class table or model and itss general for evevr also in admin panel and queries
    class Meta:
        ordering = ['created_date']



    def __str__(self):
        return "{} - {}".format(self.title, self.id)

