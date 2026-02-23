from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib import messages
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

def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {'form': form})


def product_delete(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':

        # 🔥 REGRA DE NEGÓCIO
        if product.stock > 0:
            messages.error(request, "Não é possível excluir produto com estoque maior que zero.")
            return redirect('product_list')

        product.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect('product_list')

    return render(request, 'catalog/product_confirm_delete.html', {'product': product})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/product_form.html', {'form': form})