#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/18 18:02
# @Author  : youker
# @File    : blog_tags.py
# @Contact : youkerbz@gmail.com
# @Content : 

from ..models import Article, Category
from django import template
# 需要引入template,注册为模板标签
# 实例化了一个template.Library 类，并将函数 get_recent_posts 装饰为 register.simple_tag

register = template.Library()


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:5]


@register.simple_tag
def get_dates():
    # 返回文章的创建日期，精确到月，降序排列
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categorys():
    return Category.objects.all()