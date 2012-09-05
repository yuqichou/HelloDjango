from django.conf.urls import patterns, include, url
from django.contrib import admin
from HelloDjango import settings

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
      
      
      url(r'^news/index', 'news.views.index'),
      url(r'^news/article/list', 'news.views.article_list'),
      url(r'^news/article/(?P<article_id>\d+)', 'news.views.article_detail'),
      
      url(r'^news/comment/list/(?P<article_id>\d+)', 'news.views.comment_list'),
      url(r'^news/comment/add', 'news.views.comment_add'),
      
#      url(r'^news/articleList.html', ListView.as_view(queryset=Article.objects,
#                                                     context_object_name='article_list',
#                                                     template_name='articleList.html')),
)

 
urlpatterns += patterns('', 
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH, 'show_indexes':True}), 
            ) 




