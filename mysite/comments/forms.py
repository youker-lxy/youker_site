#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/04/20 09:43
# @Author  : youker
# @File    : forms.py
# @Contact : youkerbz@gmail.com
# @Content : 
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    类似ORM。
    如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），
    那么使用 ModelForm 类会简单很多
    """
    # 该内部类指定与表单的相关
    class Meta:
        # 指定对应数据库的模型类
        model = Comment
        # 指定要在表单中显示的字段
        fields = ['name', 'email', 'url', 'text']
