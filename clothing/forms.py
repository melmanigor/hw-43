from django import forms
from .models import ClothingModel

class ClothingForm(forms.Form):
    name = forms.CharField(max_length=100)

class ClothingCreateForm(forms.ModelForm):
    class Meta:
        model = ClothingModel
        fields = ['name', 'manufacturer', 'price', 'type']
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if len(name)<=3 or len(name)>=100:
            raise forms.ValidationError("Name must be between 3 and 100 characters.")
        return name
    def clean_price(self):
        price=self.cleaned_data.get('price')
        if price<0 or price>1000:
            raise forms.ValidationError("Price must be between 0 and 1000.")
        return price