from django.urls import path
from .views import SignupView,LoginView,LogoutView,AdminUserView ,AdminUserDeleteView,AdminUserCreateView

urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'),
    #path('signup/', signup_view, name='signup'),
    #path('login/', login_view, name='login'),
    #path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin-user/', AdminUserView.as_view(), name='admin_user_list'),
    path('admin-user/<int:pk>/delete/', AdminUserDeleteView.as_view(), name='admin_user_delete'),
    path('admin-user/create/', AdminUserCreateView.as_view(), name='admin_user_create'),

]