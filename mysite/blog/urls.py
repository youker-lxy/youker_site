#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/06 09:30
# @Author  : youker
# @File    : urls.py
# @Contact : youkerbz@gmail.com
# @Content : 


from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'article/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    path(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    path(r'category/(?P<pk>[0-9]+)/', views.category, name='category')
]
