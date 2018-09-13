
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.list_brands, name='list_brands'),
    path('create', views.create_brand, name='create_brand'),
    path('update/<int:id>', views.update_brand, name='update_brand'),
    path('inactive', views.list_brands_inactive, name='list_brands_inactive'),
    path('update_inactive/<int:id>', views.update_inactive_brand, name='update_inactive_brand'),


]
