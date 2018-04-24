# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import KemiBox, Post
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,
                                  FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
import pdb

class AjaxResponseMixin:

	def render_to_response(self, context, **response_kwargs):
		json_payload=serializers.serialize('json',context['object_list'])
		return JsonResponse({'status':True, 'data':json_payload})

		
class HomeView(TemplateView):
	template_name='index.html'


class KemiBox_list( AjaxResponseMixin, ListView):
	model=KemiBox
	

	def get_queryset(self):
    
	    return KemiBox.objects.all()


class Post_list(AjaxResponseMixin, ListView):
	model=Post

	def get_queryset(self):
		kemi_box=KemiBox.objects.get(id=1)
		return Post.objects.filter(kemibox=kemi_box)
