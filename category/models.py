from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
# from django.utils import


class Category(models.Model):


    category_name  =   models.CharField(max_length=100)
    category_description   =   models.TextField()
    # is_active   =   models.BooleanField(choices=STATUS_CHOICES, default=1)
    is_active   =   models.BooleanField(default=True)
    created_by  =   models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  =   models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at  =   models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.category_name
