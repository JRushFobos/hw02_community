from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:settings.NUM_POSTS]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:settings.NUM_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
