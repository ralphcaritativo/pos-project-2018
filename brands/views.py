from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def list_brands(request):
    brands = Brand.objects.all().filter(is_active=True).order_by('brand_name')

    return render(request, 'brands/list_brands.html', {'brands': brands})


def create_brand(request):
    form = BrandForm(request.POST or None)
    brand = Brand.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        last_saved = Brand.objects.latest('created_at')
        messages.success(request, "{} successfully created!".format(last_saved))
        return redirect('list_brands')

    return render(request, 'brands/brand_form.html', {'form': form})

def update_brand(request, id):
    brands = get_object_or_404(Brand, id=id)
    # brands = Brand.objects.get(id=id)
    form = BrandForm(request.POST or None, instance = brands)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(brands.brand_name))
        return redirect('list_brands')

    return render(request, 'brands/brand_form.html', {'form': form, 'brands': brands})


def list_brands_inactive(request):
    brands = Brand.objects.all().filter(is_active=False).order_by('brand_name')

    return render(request, 'brands/list_brands_inactive.html', {'brands': brands})


def update_inactive_brand(request, id):
    brands = get_object_or_404(Brand, id=id)
    # brands = Brand.objects.get(id=id)
    form = BrandForm(request.POST or None, instance = brands)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(brands.brand_name))
        return redirect('list_brands_inactive')

    return render(request, 'brands/brand_inactive_form.html', {'form': form, 'brands': brands})
