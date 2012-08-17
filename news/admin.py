from django.contrib import admin
from news.models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    list_per_page=15

class AuthorAdmin(admin.ModelAdmin):
    list_per_page=15



admin.site.register(Article,ArticleAdmin);
admin.site.register(Author,AuthorAdmin);