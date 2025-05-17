from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import PositionModel,WorkerModel
from .forms import WorkerForm, AdminVerifyForm
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

def worker_list(request):
    position_id=request.GET.get('position')

    if position_id:
        workers=WorkerModel.objects.filter(position_id=position_id)
    else:
        workers=WorkerModel.objects.all()

    positions=PositionModel.objects.all()

    return render(request, 'workers/workers_list.html',{
        'workers':workers,
        'positions':positions,
        'selected_position':int(position_id) if position_id else None
                                
    })
def add_worker(request):
    if not is_verified_admin(request):
        return HttpResponseForbidden("Only admin can access this page")
    if request.method=='POST':
        form=WorkerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            del request.session['verified_admin_email']
            return redirect('worker_list')
    else:
        form=WorkerForm()
    return render(request, 'workers/add_worker.html', {'form':form})
def update_worker(request,pk):
    if  not is_verified_admin(request):
        return HttpResponseForbidden("Only admin can access this page")

    item=get_object_or_404(WorkerModel,pk=pk)
    

    if request.method=='POST':
        form=WorkerForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form=WorkerForm(instance=item)
    return render(request,'workers/update_worker.html',{
        'form':form,
        'item':item
        })
def delete_worker(request,pk):
    if not is_verified_admin(request):
        return HttpResponseForbidden("Only admin can access this page")
    item=get_object_or_404(WorkerModel,pk=pk)
    admin=request.session.get('verified_admin_email')
    if item.email==admin:
        messages.error(request,"You can't delete Administrator")
        return redirect('worker_list')
    if request.method=='POST':
        item.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('worker_list')
    return render(request,'workers/delete_worker.html',{'worker':item})

