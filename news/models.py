# coding:utf8
from django.db import models

class Author(models.Model):
    name = models.CharField('作者姓名',max_length=40)
    email = models.EmailField('email',blank=True)
    head_photo=models.ImageField('作者照片',upload_to='author_photos/%Y/%m/%d/',blank=True)
    
    
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
    attachment=models.FileField('文章附件',upload_to='attachment/%Y/%m/%d/',blank=True)
    
    class Meta:  
        verbose_name = "文章信息"  
        verbose_name_plural = "文章信息"  
    
    def __unicode__(self):
        return self.title
    

class Comment(models.Model):
    text=models.CharField('评论内容',max_length=80)
    pub_date = models.DateTimeField('发布时间')
    ip_addr=models.IPAddressField('评论ip',blank=True)
    comment_user=models.CharField('评论人',max_length=50,blank=True)
    article=models.ForeignKey(Article)
    
    class Meta:  
        verbose_name = "文章评论"  
        verbose_name_plural = "文章评论"  
    
    def __unicode__(self):
        return self.text
    
    
    
