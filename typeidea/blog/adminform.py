# coding:utf-8

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from dal import autocomplete 
from django import forms

from .models import Category, Tag, Post 

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)
    category = forms.ModelChoiceField(
                queryset=Category.objects.all(),
                widget=autocomplete.ModelSelect2(url='category-autocomplete'),
                label='分类',
    )
    tags = forms.ModelMultipleChoiceField(
                queryset=Tag.objects.all(),
                widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
                label='标签',
    )


    class Meta:
        model=Post 
        fields = ('title','desc','content','category','is_markdown','tags','status')
