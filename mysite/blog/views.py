from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def index(request):
    # return HttpResponse('欢迎访问我的博客首页~')
    # return render(request,'blog/index.html', context={
    #     'title': '我的博客首页',
    #     'welcome': '欢迎问我的博客首页！！！'
    # })

    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', context={'article': article})