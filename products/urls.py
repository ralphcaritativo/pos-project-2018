
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.list_product, name='list_product'),
    path('create', views.create_product, name='create_product'),
    path('update/<int:id>', views.update_product, name='update_product'),
    path('inactive', views.list_product_inactive, name='list_product_inactive'),
    path('update_inactive/<int:id>', views.update_inactive_product, name='update_inactive_product'),


]
