from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.clothing_search, name='clothing_search'),
    path('add/', views.add_clothing, name='add_clothing'),
]