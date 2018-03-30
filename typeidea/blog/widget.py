# -*- coding: utf-8 -*-

from markdownx.widgets import AdminMarkdownxWidget


class CustomAdminMarkdownWidget(AdminMarkdownxWidget):
    class Media:
        extend = False
        css = {
            'all': [
                'css/markdownx.css',
                'css/markdownx-skin/desert.css',
            ]
        }
        js = [
            'markdownx/js/markdownx{}.js'.format('.min'),
            'js/prettify.js',
            'js/markdownx-widget.js',
        ]
