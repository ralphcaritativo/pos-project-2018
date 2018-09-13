
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.list_category, name='list_category'),
    path('create', views.create_category, name='create_category'),
    path('update/<int:id>', views.update_category, name='update_category'),
    path('inactive', views.list_category_inactive, name='list_category_inactive'),
    path('update_inactive/<int:id>', views.update_inactive_category, name='update_inactive_category'),


]
