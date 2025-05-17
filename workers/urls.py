from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('verify_admin/', views.verify_admin, name='verify_admin'),
    path('add/', views.add_worker, name='add_worker'),
    path('update/<int:pk>/', views.update_worker, name='update_worker'),
    path('delete/<int:pk>/', views.delete_worker, name='delete_worker'),
    
    
]