# Standard library import
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View

# Local import
from .models import Product
from .forms import Searchform


def product_list(request):
    products = Product.objects.filter(available=True)
    form = Searchform()
    if 'search' in request.GET:
        form = Searchform(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            products = products.filter(
                Q(title__icontains=data) |
                Q(description__icontains=data)
            )
    context = {
        'products': products, 'form': form
    }
    return render(request, '', context)


def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id)
    return render(request, '', {'product': product})