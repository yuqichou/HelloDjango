# coding:utf8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils import timezone
from news.models import Article, Comment


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


#首页
def index(request):
    return render_to_response('index.html')

#文章列表
def article_list(request):
    
    
    article_list = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(article_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    
    return render_to_response('articleList.html',
                              {'articles': articles},
                              context_instance=RequestContext(request))
    
    
#文章详细
def article_detail(request,article_id):
    
    try:
        article=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse('ni ma article not exist')
    
    return render_to_response('articleDetail.html',
                              {'article':article},
                              context_instance=RequestContext(request))
    
    
    
#添加评论
def comment_add(request):
    comment = Comment(text=request.POST.get('comment_text'),
                      article=Article(id=request.POST.get('article_id')),
                      comment_user=request.POST.get('comment_user'),
                      pub_date=timezone.now(),
                      ip_addr=get_client_ip(request))
    comment.save()
    return redirect('news.views.comment_list', article_id=request.POST.get('article_id'))

#评论列表
def comment_list(request,article_id):
    
    try:
        articleParam=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse('ni ma article not exist')
    
    
    comment_list = Comment.objects.filter(article=articleParam)
    paginator = Paginator(comment_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)
    
    return render_to_response('commentList.html',
                              {'comments': comments,
                               'article':articleParam},
                              context_instance=RequestContext(request))
    
    

    
    
    
    
    
    
    