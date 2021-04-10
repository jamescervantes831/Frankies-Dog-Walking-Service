from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/users')
    else:
        form = RegisterForm()   
    return render(response, 'registrar/register.html', {"form": form}
    )

# login view 
def login(request):
    return render(request, 'registrar/login.html')