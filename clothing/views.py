from django.shortcuts import render
from.models import ClothingModel, TypeModel

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