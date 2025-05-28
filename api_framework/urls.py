from django.urls import path
from .views import ClothingListCreateAPIView, ClothingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('clothes/', ClothingListCreateAPIView.as_view(), name='api_clothing_list'),
    path('clothes/<int:pk>/', ClothingRetrieveUpdateDestroyAPIView.as_view(), name='api_clothing_detail'),
]