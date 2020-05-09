from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    login_url = 'account_login'



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    login_url = 'account_login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    fields = ('title', 'body')
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
