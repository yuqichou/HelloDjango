# coding:utf8
from django import forms
from django.contrib import admin
from news.models import Article, Author, Comment
from HelloDjango import settings

import sys
reload(sys)
sys.setdefaultencoding('utf-8')  

class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('title', 'pub_date')
    search_fields = ['title']
    list_filter = ['pub_date','authors']

class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 15
    
    def show_head_photo(self,obj):
        
        if(len(obj.head_photo.name)>0):
            return '<a target="blank" href="'+settings.MEDIA_URL+obj.head_photo.name+'">'+'查看'+'</a>'
        else:
            return ''
    
    show_head_photo.short_description='作者照片地址'
    show_head_photo.allow_tags=True
    
    search_fields = ['name']
    list_display = ('name', 'email','show_head_photo')


class CommentModelForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment

class CommentAdmin(admin.ModelAdmin):
    list_per_page = 15
    form = CommentModelForm
    list_display = ('text', 'pub_date','comment_user','article')
    list_filter = ['pub_date']
    search_fields = ['text']

admin.site.register(Article, ArticleAdmin);
admin.site.register(Author, AuthorAdmin);
admin.site.register(Comment, CommentAdmin);
