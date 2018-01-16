# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import connection #引入数据库的列表
from django.views.generic import ListView, DetailView

from .models import Post,Tag,Category 
from config.models import SideBar 
from comment.models import Comment

class BasePostsView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class IndexView(BasePostsView):
    pass

class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(Category_id=cate_id)
        return qs

class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.posts.all()
        return posts 

class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'



def get_common_context():
    categories = Category.objects.filter(status=1)

    nav_cates=[]
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)
    
    side_bars = SideBar.objects.filter(status=1)
    
    recently_posts = Post.objects.filter(status=1)[:10]
    #`hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'nav_cates':nav_cates,
        'cates':cates,
        'side_bars':side_bars,
        'recently_comments':recently_comments,
        'recently_posts':recently_posts,
    }
    return context



