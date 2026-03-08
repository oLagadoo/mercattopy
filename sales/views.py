from django.shortcuts import render, redirect
from django.contrib import messages
from catalog.models import Product
from .models import Sale, SaleItem


def create_sale(request):

    products = Product.objects.filter(is_active=True)

    if request.method == "POST":

        product_id = request.POST.get("product")
        quantity = int(request.POST.get("quantity"))

        product = Product.objects.get(id=product_id)

        if quantity > product.stock:
            messages.error(request, "Estoque insuficiente para realizar a venda.")
            return redirect("create_sale")

        sale = Sale.objects.create()

        unit_price = product.price
        subtotal = unit_price * quantity

        SaleItem.objects.create(
            sale=sale,
            product=product,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )

        sale.total = subtotal
        sale.save()

        product.stock -= quantity
        product.save()

        messages.success(request, "Venda registrada com sucesso!")

        return redirect("product_list")

    return render(request, "sales/sale_form.html", {"products": products})