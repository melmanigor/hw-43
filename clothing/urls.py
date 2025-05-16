from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.clothing_search, name='clothing_search'),
    path('add/', views.add_clothing, name='add_clothing'),
    path('<int:pk>/', views.clothing_detail, name='clothing_detail'),
    path('update/<int:pk>/', views.update_clothing, name='update_clothing'),
    path('delete/<int:pk>/', views.delete_clothing, name='delete_clothing'),
]