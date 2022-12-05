from django.shortcuts import render, get_object_or_404
from .models import Product



def more(request):
    post = Product.objects.order_by('-title')
    return render(request, 'index.html', {'post': post})


def detail(request,id):
    home = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'home': home})

