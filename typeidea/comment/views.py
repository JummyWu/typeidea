# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect 
from django.views.generic import TemplateView

from .forms import CommentForm 
from .models import Comment 


class CommentShowMixin(object):
    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)
        return comments 

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form':CommentForm(),#initial={'target':self.request.path})  
            'comment_list':self.get_comments(),
        })
        return super(CommentShowMixin, self).get_context_data(**kwargs)


class CommentView(TemplateView):
    template_name='comment/result.html'
    http_method_names= ['post',]

    def post(self, request, *args,**kwargs):
        comment_form =CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance=comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed=True
            return redirect(target)
        else:
            succeed=False

        context = {
            'succeed':succeed,
            'form':comment_form,
            'target':target,
        }
        return self.render_to_response(context)

