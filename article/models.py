from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content=models.CharField(max_length=2000)
    
    
    def __unicode__(self):
        return self.title
    

