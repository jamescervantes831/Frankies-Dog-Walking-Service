from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from users import validations as v
from django import forms
#from users import models as user_models
#from walkers import models as walker_models

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        validators=[validators.EmailValidator()]
    )
    password= forms.CharField(
        max_length=15,
        validators=[v.validate_password]
    )
    name= forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            'name', 
            'password1', 
            'password2'
        ]