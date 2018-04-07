from django.http import HttpResponse
from django.shortcuts import render
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
