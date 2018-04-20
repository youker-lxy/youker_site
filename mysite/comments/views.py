from django.shortcuts import render, get_object_or_404, redirect
from ..blog.models import Article
from .forms import CommentForm
# Create your views here.

def post_comment(request, article_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    article = get_object_or_404(Article, article_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':

        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 用这些数据构造了 CommentForm 的实例，这样表单就生成了。
        # 即用请求数据构造表单，包含数据
        form = CommentForm(request.POST)

        # 检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 数据合法
            # commit=False 仅仅用表单的数据生成 Comment 模型类的实例，
            # 但还不保存评论数据到数据库。
            # 即用表单的数据构造 评论模型类的实例，这个实例save才将数据保存到数据库
            comment = form.save(commit=False)
            # 将评论与对应文章关联
            comment.article = article
            comment.save()

            # 当redirect 函数接收一个模型的实例时，
            # 那么这个实例必须实现了get_absolute_url 方法
            # 它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(article)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 article.comment_set.all() 方法，
            # 这个用法有点类似于 article.objects.all()
            # 其作用是获取这篇 article 下的的全部评论，
            # 因为 article 和 Comment 是 ForeignKey 关联的，
            # 因此使用 article.comment_set.all() 反向查询全部评论。
            comment_list = article.comment_set.all()
            context = {'article': article,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog:detail.html', context=context)
    # 非POST请求，直接重新加载该文章详情页
    return redirect(article)