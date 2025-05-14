from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:pk>/', views.clothing_reviews, name='clothing_reviews'),
    path('add/<int:pk>/', views.add_review, name='add_review'),
]