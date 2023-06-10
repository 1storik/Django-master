# blog/views.py
from django.db.models import Avg, Subquery, OuterRef
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm, RatingForm
from .models import Post, Rating
from django.shortcuts import render, redirect


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-ratings__value', '-pk')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = Rating.objects.order_by('-value')
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['ratings'] = post.ratings.all()
        return context


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('home')
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post_delete.html'


def add_rating(request, pk):
    post = Post.objects.get(pk=pk)
    rating = post.ratings.first()  # Get the first rating associated with the post

    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)  # Pass the rating instance to the form
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = RatingForm(instance=rating)  # Pass the rating instance to the form

    return render(request, 'add_rating.html', {'form': form, 'post': post})

