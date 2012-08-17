# coding:utf8
from django.db import models

class Author(models.Model):
    name = models.CharField('作者姓名',max_length=40)
    email = models.EmailField('email',blank=True)
    
    class Meta:  
        verbose_name = "作者信息"  
        verbose_name_plural = "作者信息"  
    
    def __unicode__(self):
        return self.name



class Article(models.Model):
    title = models.CharField('文章标题',max_length=200)
    pub_date = models.DateTimeField('发布时间')
    content=models.TextField('文章内容')
    authors = models.ManyToManyField(Author,verbose_name="作者")
    
    class Meta:  
        verbose_name = "文章信息"  
        verbose_name_plural = "文章信息"  
    
    def __unicode__(self):
        return self.title
