from django.urls import path
from .views import ClothingListAPIView, ClothingDetailAPIView

urlpatterns = [
    path('clothes/', ClothingListAPIView.as_view(), name='api_clothing_list'),
    path('clothes/<int:pk>/', ClothingDetailAPIView.as_view(), name='api_clothing_detail'),
]
