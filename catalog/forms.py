from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError("Preço não pode ser negativo.")

        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name and len(name) < 3:
            raise ValidationError("Nome deve ter pelo menos 3 caracteres.")

        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if category and not category.is_active:
            raise ValidationError("Não é possível usar uma categoria inativa.")

        return category

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')

        if stock is not None and stock < 0:
            raise ValidationError("Estoque não pode ser negativo.")

        return stock