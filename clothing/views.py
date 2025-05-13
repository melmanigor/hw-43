from django.shortcuts import render,redirect
from.models import ClothingModel, TypeModel
from .forms import ClothingForm, ClothingCreateForm

# Create your views here.
def product_list(request):
    type_id=request.GET.get('type')
    if type_id:
        clothes=ClothingModel.objects.filter(type_id=type_id)
    else:
        clothes=ClothingModel.objects.all()
    
    types=TypeModel.objects.all()
  
    
    return render(request, 'clothing/product_list.html',{
        'clothes':clothes,
        'types':types,
        'selected_type':int(type_id) if type_id else None
    })
def clothing_search(request):
    clothes = []
    if request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            clothes = ClothingModel.objects.filter(name__icontains=name)
            
    else:
        form = ClothingForm()

    return render(request, 'clothing/clothing_search.html', 
                  {'form': form,
                   'clothes':clothes
                   })
def add_clothing(request):
    if request.method == 'POST':
        form = ClothingCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ClothingCreateForm()
    return render(request, 'clothing/add_clothing.html', {'form': form})