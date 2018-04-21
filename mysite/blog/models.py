# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


# 分类
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

# 文章
class Article(models.Model):
    title = models.CharField(max_length=100)
    # 大段文本内容
    body = models.TextField()
    # 创建以及最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 一对多
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 多对多
    tags = models.ManyToManyField(Tag, blank=True)
    # 内置应用模型user 用于用户管理
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 利用reverse函数，通过命名空间找到对应path，传入参数解析为具体的文章的对应url
        # 反解析url以直接访问其它视图方法。
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']