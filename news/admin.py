from django import forms
from django.contrib import admin
from news.models import Article, Author, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('title', 'pub_date')
    search_fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 15




class CommentModelForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment

class CommentAdmin(admin.ModelAdmin):
    list_per_page = 15
    form = CommentModelForm
    list_display = ('text', 'pub_date','comment_user','article')
    search_fields = ['text']

admin.site.register(Article, ArticleAdmin);
admin.site.register(Author, AuthorAdmin);
admin.site.register(Comment, CommentAdmin);
