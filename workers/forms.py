from django import forms
from .models import WorkerModel

class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerModel
        fields = ['name', 'salary', 'email', 'position']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
        }