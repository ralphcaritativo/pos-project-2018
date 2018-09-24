from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def list_product(request):
    products = Product.objects.all().filter(is_active=True).order_by('product_name')

    return render(request, 'products/list_product.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)
    product = Product.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        last_saved = Product.objects.latest('created_at')
        messages.success(request, "{} successfully created!".format(last_saved))
        return redirect('list_product')

    return render(request, 'products/product_form.html', {'form': form})

def update_product(request, id):
    products = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance = products)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(products.product_name))
        return redirect('list_product')

    return render(request, 'products/product_form.html', {'form': form, 'products': products})


def list_product_inactive(request):
    products = Product.objects.all().filter(is_active=False).order_by('product_name')

    return render(request, 'products/list_product_inactive.html', {'products': products})


def update_inactive_product(request, id):
    products = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance = products)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(products.product_name))
        return redirect('list_product_inactive')

    return render(request, 'products/product_inactive_form.html', {'form': form, 'products': products})
