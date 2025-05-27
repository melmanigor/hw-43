from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from.models import ClothingModel, TypeModel
from .forms import ClothingForm, ClothingCreateForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy
import requests
# Create your views here.
class ClothingListView(ListView):
    model = ClothingModel
    template_name = 'clothing/product_list.html'
    context_object_name='clothes'
    def get_queryset(self):
        queryset = super().get_queryset()
        type_id = self.request.GET.get('type')
        if type_id:
            queryset = queryset.filter(type_id=type_id)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = TypeModel.objects.all()
        context['selected_type'] = int(self.request.GET.get('type')) if self.request.GET.get('type') else None
        return context
class ClothingSearchView(FormView):
    form_class = ClothingForm
    template_name = 'clothing/clothing_search.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        clothes = ClothingModel.objects.filter(name__icontains=name)
        return self.render_to_response(self.get_context_data(form=form, clothes=clothes))
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# class AddClothingView(CreateView):
#     model = ClothingModel
#     form_class = ClothingCreateForm
#     template_name = 'clothing/add_clothing.html'
#     success_url = reverse_lazy('product_list')

#     def form_valid(self, form):
#         messages.success(self.request, 'Item added successfully')
#         return super().form_valid(form)
#     def form_invalid(self, form):
#         messages.error(self.request, 'Please correct the errors below.')
#         return super().form_invalid(form)

class ClothingCreateView(CreateView):
    model = ClothingModel
    form_class = ClothingCreateForm
    template_name = 'clothing/add_clothing.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        
        name=form.cleaned_data.get('name')
       
        if  ClothingModel.objects.filter(name__iexact=name).exists():
            messages.error(self.request, 'Item already exists')
            return self.form_invalid(form)
        messages.success(self.request, 'Item added successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class ClothingDetailView(DetailView):
    model=ClothingModel
    template_name='clothing/clothing_detail.html'
    context_object_name='item'

class ClothingUpdateView(UpdateView):
    model=ClothingModel
    template_name='clothing/update_clothing.html'
    fields=['name','price','type']
    success_url=reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Item updated successfully')     
        return super().form_valid(form)
    
    def form_invalid(self, form):
       
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)
class ClothingDeleteView(DeleteView):
    model=ClothingModel
    template_name='clothing/delete_clothing.html'
    success_url=reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Item deleted successfully')
        print('Item deleted successfully')
        return super().form_valid(form)
def coming_soon(request):
    url = 'https://dummyjson.com/products/category/mens-shirts'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        products = data.get('products', [])
    except requests.exceptions.RequestException as e:
        products = []
        print(f"Error fetching data: {e}")

    return render(request, 'clothing/coming_soon.html', {'products': products})

