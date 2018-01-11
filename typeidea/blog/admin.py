# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag
from typeidea.custom_site import custom_site

@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','owner','created_time']
    list_display_links = ['category','status']

    list_filter = ['category','owner']
    search_fields = ['title','category__name','owner__username']
    save_on_top = True
    show_full_result_count = False
    
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'created_time'
    list_editable = ('title',)

    #编辑页面
    save_on_top = True
    #exclude = ('owner',)#不展示字段:w
    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (('category', 'title'), 'content')
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),
            'fields': ('tags', ),
        }),
    )

@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass
