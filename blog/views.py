from django.shortcuts import redirect, render
from django.urls import reverse_lazy 
from .models import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from .forms import NewCommentForm




class CustomLoginView(LoginView):
    pass
    # template_name = 'login.html'
    # fields = '__all__'
    # redirect_authenticated_user = True

    # def get_success_url(self):
    #     return reverse_lazy('home')





#use LoginRequiredMixin for only logged in users to see the listview
class BlogListView( ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'




class BlogDetailView( DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        new_comment = BlogComment()
        return self.get(self, request, *args, **kwargs)



class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
