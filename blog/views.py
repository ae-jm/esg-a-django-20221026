from django.shortcuts import render
from blog.models import Post

def index(request):
    post_qs = Post.objects.all().order_by('-id')
    return render(request, "blog/index.html", {
        "posts":post_qs,
    })

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog\single_post_page.html", {
        "post":post,
    })
