from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comentario, Dislike
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PostListView(ListView):
    model = Post

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comentario = form.instance
            comentario.usuario = self.request.user
            comentario.post = post
            comentario.save()
            return redirect('detail', slug=post.slug)
        return redirect('detail', slug=self.get_object().slug)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form' : CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)

        # if self.request.user.is_authenticated:
        PostView.objects.get_or_create(usuario=self.request.user, post=object)

        return object

class PostUpdateView(UpdateView):
    form_class=PostForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'update'
        })
        return context

class PostCreateView(CreateView):
    form_class=PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'create'
        })
        return context
    

class PostDeleteView (DeleteView):
    model = Post
    success_url = '/'

def like(request,slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs =Like.objects.filter(usuario=request.user, post=post)
    dislike_qs =Dislike.objects.filter(usuario=request.user, post=post)


    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    elif dislike_qs.exists():
        dislike_qs[0].delete()
        Like.objects.create(usuario=request.user, post=post)
        return redirect('detail', slug=slug)
    
    Like.objects.create(usuario=request.user, post=post)
    return redirect('detail', slug=slug)

def dislike(request,slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs =Like.objects.filter(usuario=request.user, post=post)
    dislike_qs =Dislike.objects.filter(usuario=request.user, post=post)

    if dislike_qs.exists():
        dislike_qs[0].delete()
        return redirect('detail', slug=slug)
    elif like_qs.exists():
        like_qs[0].delete()
        Dislike.objects.create(usuario=request.user, post=post)
        return redirect('detail', slug=slug)
    
    Dislike.objects.create(usuario=request.user, post=post)
    return redirect('detail', slug=slug)
