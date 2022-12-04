from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_PER_PAGE = 10


def index(request):
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    template = 'posts/index.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'posts': posts,
        'group': group
    }
    return render(request, template, context)
