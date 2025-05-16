from django.shortcuts import render,redirect,get_object_or_404
from.models import ClothingModel, TypeModel
from .forms import ClothingForm, ClothingCreateForm
from django.contrib import messages

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

def clothing_detail(request,pk):
    item=get_object_or_404(ClothingModel,pk=pk)
    return render(request,'clothing/clothing_detail.html',{'item':item})
def update_clothing(request,pk):
    item=get_object_or_404(ClothingModel,pk=pk)

    if request.method=='POST':
        form=ClothingCreateForm(request.POST,instance=item)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=ClothingCreateForm(instance=item)
    return render(request,'clothing/update_clothing.html',{'form':form,'item':item})

def delete_clothing(request,pk):
    item=get_object_or_404(ClothingModel,pk=pk)
    if request.method=='POST':
        item.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('product_list')
    return render(request,'clothing/delete_clothing.html',{'item':item})
