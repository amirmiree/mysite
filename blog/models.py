from django.db import models
# data base --> create table the name is : app_name-class-name --> coulns --> filds
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    # tag
    # imgae
    # author
    # category
    content_viwe = models.IntegerField(default = 0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null = True)
    created_date= models.DateField(auto_now_add= True)
    updated_date= models.DateField(auto_now=True)


    def __str__(self):
        return "{} - {}".format(self.title, self.id)