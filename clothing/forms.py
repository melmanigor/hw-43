from django import forms
from .models import ClothingModel

class ClothingForm(forms.Form):
    name = forms.CharField(max_length=100)

class ClothingCreateForm(forms.ModelForm):
    class Meta:
        model = ClothingModel
        fields = ['name', 'manufacturer', 'price', 'type']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }
    
