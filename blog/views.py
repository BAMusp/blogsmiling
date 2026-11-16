from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    ordering = ['-data_postagem']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})


class CategoryListView(ListView):
    model = Category


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = category.posts.order_by('-data_postagem')
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
        'category': category,
    })