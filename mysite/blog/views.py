from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article,Category
from mysite.comments.forms import CommentForm

import markdown
import pygments
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
    # 文章内容使用markdown格式，顶部引入Markdown模块
    # article.body = markdown.markdown(article.body, extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                               ])

    # markdown参数变动，没有extensions默认参数,映入pygenmts高亮。。重启服务器，刷新浏览器。。这是一个玄学。。。
    article.body = markdown.markdown(article.body, ['extra', 'codehilite', 'toc', ])

    # 导入表单类，便于传入模板渲染出表单
    form = CommentForm()

    # 获取这篇文章下的全部评论
    comment_list = article.comment_set.all()

    # return render(request, 'blog/detail.html', context={'article': article})
    # 修改传递给模板的参数
    context = {
        'article': article,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context=context)


# 根据年月过滤文章
def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month
                                          ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


# 获取分类
def category(request, pk):
    # 找具体某个分类时，需要传入pk,调用get_object_or_404进行查找
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})