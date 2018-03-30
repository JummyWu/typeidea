# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='名称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width:60%'}
        )
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width:60%'}
        )
    )
    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': 'width:60%'}
        )
    )
    content = forms.CharField(
        label='内容',
        max_length=100,
        widget=forms.widgets.Textarea(attrs={'row': 6, 'cols': 80, 'class': 'form-control'})
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('长度怎么这么短呢!')
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
