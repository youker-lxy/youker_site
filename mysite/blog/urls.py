#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/06 09:30
# @Author  : youker
# @File    : urls.py
# @Contact : youkerbz@gmail.com
# @Content : 


from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
]
