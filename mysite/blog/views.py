from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, post, day, month, year):
    try:
        post = get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            publish__day=day,
            publish__month=month,
            publish__year=year,
            slug=post,
        )
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "blog/post/detail.html", {"post": post})
