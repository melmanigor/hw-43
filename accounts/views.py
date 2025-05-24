from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
class SignupView(SuccessMessageMixin,CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
    success_message = "Account created successfully"
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

# #def signup_view(request):
#     if request.method == 'POST':
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             messages.success(request, 'Account created successfully')
#             return redirect('home')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form=UserRegisterForm()


#     return render(request, 'accounts/signup.html',{'form':form})


class LoginView(SuccessMessageMixin,LoginView):
    template_name = 'accounts/login.html'
    success_message = "Logged in successfully"

# def login_view(request):
   
#     if request.method == 'POST':
       
#         form = AuthenticationForm(request, data=request.POST)
       
#         if form.is_valid():
         
#             user = form.get_user()
            
#             login(request, user)
#             messages.success(request, f'Logged in as {user.username}')
#             return redirect('home')
#         else:
            
#             messages.error(request, 'Invalid username or password.')
#     else:
    
#         form = AuthenticationForm()
    
#     return render(request, 'accounts/login.html', {'form': form})


class LogoutView(LogoutView):
    next_page = reverse_lazy('home')    


# def logout_view(request):
#     logout(request)
#     messages.success(request, "You have been logged out.")
#     messages.success(request, 'Logged out successfully')
#     return redirect('home')
class AdminUserCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/admin_user_create.html'
    success_url = reverse_lazy('admin_user_list')
    def test_func(self):
        return self.request.user.is_superuser
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"User '{form.instance.username}' created successfully")
        return response
class AdminUserView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    model = User
    template_name = 'accounts/admin_user_list.html'
    context_object_name = 'users'
    def test_func(self):
        return self.request.user.is_superuser
class AdminUserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'accounts/admin_user_confirm_delete.html'
    success_url = reverse_lazy('admin_user_list')
    context_object_name = 'user_to_delete'
    def test_func(self):
        return self.request.user.is_superuser
    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'User deleted successfully')
        return super().post(request, *args, **kwargs)
    