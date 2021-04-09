from django.shortcuts import render

from .models import Walker, Walker_Appointment, Review, Walker_Appointment
# Create your views here.

def index(request):
    return render(request, 'walkers/index.html')
