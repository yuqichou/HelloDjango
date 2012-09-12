# coding:utf8
from django.core.files.storage import FileSystemStorage
from django.db import models
import tempfile

# Create your models here.

temp_storage_location = tempfile.mkdtemp()
temp_storage = FileSystemStorage(location=temp_storage_location)

class Consumer(models.Model):
    username=models.CharField('用户登录名',max_length=50,unique=True)
    password=models.CharField('用户登录密码',max_length=150)
    nickname=models.CharField('用户昵称',max_length=50,unique=True)
    
    avatar_small=models.ImageField('用户照片(小)',upload_to='users/%Y/%m/%d/small',blank=True,null=True)
    avatar_origin=models.ImageField('用户照片(原始)',upload_to='users/%Y/%m/%d/origin',blank=True,null=True)
    birthday=models.DateField(blank=True,null=True)
   
   
   
 