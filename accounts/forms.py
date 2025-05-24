from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout, Fieldset, ButtonHolder, Button


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False  
        self.helper.layout = Layout(
            Fieldset(
                'User Information',
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-success'),
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.location.href='/'")
            )
        )


