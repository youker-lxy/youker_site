#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/06 09:30
# @Author  : youker
# @File    : urls.py
# @Contact : youkerbz@gmail.com
# @Content : 


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index(), name='index'),
]
