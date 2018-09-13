from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def list_category(request):
    categorys = Category.objects.all().filter(is_active=True).order_by('category_name')

    return render(request, 'category/list_category.html', {'categorys': categorys})


def create_category(request):
    form = CategoryForm(request.POST or None)
    category = Category.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        last_saved = Category.objects.latest('created_at')
        messages.success(request, "{} successfully created!".format(last_saved))
        return redirect('list_category')

    return render(request, 'category/category_form.html', {'form': form})

def update_category(request, id):
    categorys = get_object_or_404(Category, id=id)
    # brands = Brand.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance = categorys)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(categorys.category_name))
        return redirect('list_category')

    return render(request, 'category/category_form.html', {'form': form, 'categorys': categorys})


def list_category_inactive(request):
    categorys = Category.objects.all().filter(is_active=False).order_by('category_name')

    return render(request, 'category/list_category_inactive.html', {'categorys': categorys})


def update_inactive_category(request, id):
    categorys = get_object_or_404(Category, id=id)
    # brands = Brand.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance = categorys)

    if form.is_valid():
        form = form.save(commit=False)
        form.created_by= request.user
        form.save()
        messages.success(request, "{} successfully updated".format(categorys.category_name))
        return redirect('list_category_inactive')

    return render(request, 'category/category_inactive_form.html', {'form': form, 'categorys': categorys})
