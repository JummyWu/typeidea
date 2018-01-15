# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
#from django.db import connection #引入数据库的列表
from django.http import Http404 
from django.shortcuts import render 

from .models import Post,Tag


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()

    page = request.GET.get('page',1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        #分页页面
        queryset = Post.objects.filter(category_id=category_id)
    elif tag_id:
        #标签
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #else:
        #queryset = Post.objects.all()
    #print(len(posts))          #把posts变成长度，才能执行到下面的部分
    #print(connection.queries)  #输出数据库的语句，看如何执行
    #import pdb;pdb.set_trace() #断点调试
    context = {
        'posts':posts,
    }
    return render(request, 'blog/list.html', context=context)

def post_detail(request, pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")

    context = {
        'post':post,
    }
    return render(request, 'blog/detail.html', context=context)
