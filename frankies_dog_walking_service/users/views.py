from django.shortcuts import render
from .models import  User, User_Appointment, Dog, Review
from walkers import models as walker_model
# Create your views here.



# index view
def index(request):
    list_of_walkers = walker_model.Walker.objects.all()
    ratings = walker_model.Review.objects.all()
    slots = walker_model.Walker_Appointment.all()
    context = { 'list_of_walkers': list_of_walkers,
                'ratings': ratings,
                'slots': slots
            }
    return render(request, 'users/index.html', context)

# login view 
def login(request):
    return render(request, 'forms/login.html')

def review(request):
    return render(request, 'forms/review.html')

def book(request):
    return render(request, 'forms/book.html')
