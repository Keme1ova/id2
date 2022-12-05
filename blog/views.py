from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_all(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'index.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})
