from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ClothingListView.as_view(), name='product_list'),
    #path('search/', views.clothing_search, name='clothing_search'),
    path('search/', views.ClothingSearchView.as_view(), name='clothing_search'),
    #path('add/', views.AddClothingView.as_view(), name='add_clothing'),
    path('add/', views.ClothingCreateView.as_view(), name='add_clothing'),
    path('<int:pk>/', views.ClothingDetailView.as_view(), name='clothing_detail'),
    path('update/<int:pk>/', views.ClothingUpdateView.as_view(), name='update_clothing'),
    path('delete/<int:pk>/', views.ClothingDeleteView.as_view(), name='delete_clothing'),
  
]