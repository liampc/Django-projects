from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class BlogListView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']