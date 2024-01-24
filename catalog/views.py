from django.shortcuts import render

from catalog.models import Category, Product


def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list':category_list
    }
    return render(request, 'catalog/category.html', context)

def products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/products.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product.html', context)