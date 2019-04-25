from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
def new_file_name(instance,filename):
     return 'images/{0}{1}'.format(get_random_string(length=10),filename)

class Reporter(models.Model):
    name=models.CharField(max_length=20)

    def n_article(self):
        return self.all__articles.count()

    def __str__(self):
        return self.name

class Aritcle(models.Model):
    heading=models.CharField(max_length=100)
    body=models.CharField(max_length=500)
    image=models.ImageField(upload_to=new_file_name,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    reporter=models.ForeignKey(Reporter,related_name='all_articles',null=True,\
        blank=True,on_delete=models.CASCADE)
        
    def __str__(self):
        return self.heading + ' ' + str(self.created)