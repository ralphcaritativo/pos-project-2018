from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from brands.models import Brand
from category.models import Category
# from django.utils import


class Product(models.Model):

    product_name         =  models.CharField(max_length=100)
    product_description  =  models.TextField()
    product_sku          =  models.CharField(max_length = 255)
    product_price        =  models.DecimalField(default = 0.00, max_digits = 9, decimal_places = 2)
    product_quantity     =  models.IntegerField(default = 0)
    product_brand        =  models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_category     =  models.ForeignKey(Category,on_delete=models.CASCADE)
    is_active            =  models.BooleanField(default=True)
    created_by           =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at           =  models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at           =  models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.product_name
