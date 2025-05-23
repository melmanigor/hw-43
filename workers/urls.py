from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkerListView.as_view(), name='worker_list'),
  
    path('verify_admin/', views.verify_admin, name='verify_admin'),
    
    path('add/', views.AddWorkerView.as_view(), name='add_worker'),
   
    path('update/<int:pk>/', views.UpdateWorkerView.as_view(), name='update_worker'),
   
    path('delete/<int:pk>/', views.WorkerDeleteView.as_view(), name='delete_worker'),
    
    
]