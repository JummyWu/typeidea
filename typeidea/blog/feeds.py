# coding:utf-8
from __future__ import unicode_literals

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.urls import reverse

from blog.models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = 'application/xml'

    def root_attributes(self):
        attrs = super(ExtendedRSSFeed, self).root_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs

    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u'content:encoded', item['content_encoded'])


class AllPostRssFeed(Feed):
    feed_type = ExtendedRSSFeed

    title = "Jummy"
    link = "https://www.jummy.top"
    author = 'Jummy'
    description = "Jummy Blog"

    def items(self):
        return Post.objects.filter(status=1).order_by('-created_time')[:10]

    def item_extra_kwargs(self, item):
        return {'content_encoded': self.item_content_encoded(item)}

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('index')

    def item_description(self, item):
        return item.desc

    def item_author_name(self, item):
        if (item.owner.get_full_name()):
            return item.owner.get_full_name()
        else:
            return item.owner

    def item_pubdate(self, item):
        return item.created_time

    def item_content_encoded(self, item):
        return item.html
