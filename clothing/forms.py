from django import forms
from .models import ClothingModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout, Fieldset, ButtonHolder, Button

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False  
        self.helper.layout = Layout(
            Fieldset(
                'Clothing Information',
                'name',
                'manufacturer',
                'price',
                'type'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-success'),
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.location.href='/clothing/'")
            )
        )