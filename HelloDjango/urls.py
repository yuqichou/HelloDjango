from article.models import Article
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.list import ListView

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^HelloDjango/', include('HelloDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      
      url(r'^$', 'article.views.index'),
      
      url(r'^cms/articleList.html', ListView.as_view(queryset=Article.objects,
                                                     context_object_name='article_list',
                                                     template_name='articleList.html')),
)



