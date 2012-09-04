# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from news.models import Article

def index(request):
    return render_to_response('index.html')



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
                              {'articles': articles})
    
    
    
def article_detail(request):
    return render_to_response('articleDetail.html',
                              {'article': Article.objects.get(id=request.GET.get('id'))})