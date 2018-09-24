from django import forms
from .models import Product
from brands.models import Brand
from category.models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'product_name',
        'product_description',
        'product_sku',
        'product_price',
        'product_quantity',
        'product_brand',
        'product_category',
        'is_active'
        ]
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_brand'].queryset = Brand.objects.filter(is_active=True)
        self.fields['product_category'].queryset = Category.objects.filter(is_active=True)
