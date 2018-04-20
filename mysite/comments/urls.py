#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/20 10:30
# @Author  : youker
# @File    : urls.py
# @Contact : youkerbz@gmail.com
# @Content : 

from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path(r'comment/article/(?P<article_pk>[0-9]+)/', views.post_comment, name='post_comment'),

]