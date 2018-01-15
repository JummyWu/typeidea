# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from django.urls import reverse 
from django.utils.html import format_html

from .adminform import PostAdminForm 
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm 

    list_display = [
        'title','category','status_show','owner',
        'created_time','operator'
    ]
    list_display_links = []

    list_filter = ['category','owner']
    search_fields = ['title','category__name']
    
    save_on_top = True
    show_full_result_count = False
    
    actions_on_top = True
    actions_on_bottom = True

    #编辑页面
    save_on_top = True
    
    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tags',
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user

@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','status','is_nav','owner', 'created_time']
    #pass

@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display=['name','status','owner','created_time']
    #pass
