from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import PositionModel,WorkerModel
from .forms import WorkerForm, AdminVerifyForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def is_verified_admin(request):
    email=request.session.get('verified_admin_email')
    if not email:
        return False
    try:
        worker=WorkerModel.objects.get(email=email)
        return worker.position.name == 'Administrator'
        
    except WorkerModel.DoesNotExist:
        return False
  
def verify_admin(request):
    next_url = request.GET.get('next') or request.POST.get('next') or 'add_worker'
    if request.method=='POST':
        form=AdminVerifyForm(request.POST)
        if form.is_valid():
            request.session['verified_admin_email'] = form.cleaned_data['email']
            return redirect(next_url)
    else:
        form=AdminVerifyForm()
    return render(request, 'workers/verify_admin.html', {'form':form, 'next': next_url})

class WorkerListView(LoginRequiredMixin,ListView):
    model = WorkerModel
    template_name = 'workers/workers_list.html'
    context_object_name = 'workers'
    login_url='login'
    

    def get_queryset(self):
        position_id = self.request.GET.get('position')
        if position_id:
            return WorkerModel.objects.filter(position_id=position_id)
        return WorkerModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = PositionModel.objects.all()
        context['selected_position'] = int(self.request.GET.get('position')) if self.request.GET.get('position') else None
        return context   
class AddWorkerView(CreateView):
    model = WorkerModel
    form_class = WorkerForm
    template_name = 'workers/add_worker.html'
    success_url = reverse_lazy('worker_list')

    def dispatch(self, request, *args, **kwargs):
        if not is_verified_admin(request):
            return HttpResponseForbidden("Only admin can access this page")
        return super().dispatch(request, *args, **kwargs)  
    def form_valid(self, form):
        messages.success(self.request, 'Worker  added successfully')
        return super().form_valid(form)

      
class UpdateWorkerView(UpdateView):
    model = WorkerModel
    form_class = WorkerForm
    template_name = 'workers/update_worker.html'
    success_url = reverse_lazy('worker_list')

    def dispatch(self, request, *args, **kwargs):
        if not is_verified_admin(request):
            return HttpResponseForbidden("Only admin can access this page")
        return super().dispatch(request, *args, **kwargs)

class WorkerDeleteView(DeleteView):
    model = WorkerModel
    template_name = 'workers/delete_worker.html'
    success_url = reverse_lazy('worker_list')
    context_object_name = 'worker'

    def dispatch(self, request, *args, **kwargs):
        if not is_verified_admin(request):
            return HttpResponseForbidden("Only admin can access this page")
        self.object = self.get_object()
        admin_email = request.session.get('verified_admin_email')
        if self.object.email == admin_email:
            messages.error(request, "You can't delete Administrator")
            return redirect('worker_list')
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Worker deleted successfully')
        return super().delete(request, *args, **kwargs)