from django import forms
from .models import WorkerModel
from django.core.exceptions import ValidationError

class WorkerForm(forms.ModelForm):
    class Meta:
        model = WorkerModel
        fields = ['name', 'salary', 'email', 'position','photo']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 1000}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
        }
class AdminVerifyForm(forms.Form):
    email = forms.EmailField(label='Input your email here')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
           worker=WorkerModel.objects.get(email=email)
           if worker.position.name != 'Administrator':
                raise ValidationError("Only Administrators can add worker")
               
        
        except WorkerModel.DoesNotExist:
            raise ValidationError("Email does not exist")
        return email
    