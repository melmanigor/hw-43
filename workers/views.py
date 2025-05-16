from django.shortcuts import render,redirect, get_object_or_404
from .models import PositionModel,WorkerModel
from .forms import WorkerForm
# Create your views here.

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
