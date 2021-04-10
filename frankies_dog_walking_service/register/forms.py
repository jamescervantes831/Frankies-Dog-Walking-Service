from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users import models as user_models
from walkers import models as walker_models

class RegisterForm(UserCreationForm):
    email = 