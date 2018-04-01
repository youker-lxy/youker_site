# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 分类
class Category(models.Model):
    name = models.CharField(max_length=50)


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=50)


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