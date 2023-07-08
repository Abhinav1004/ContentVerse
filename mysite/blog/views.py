from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "blog/post/detail.html", {"post": post})
