from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.shortcuts import get_object_or_404

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {
        'product': product
    })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {
        'categories': categories
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {
        'products': products
    })

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def logout_view(request):
    return render(request, 'auth/login.html')