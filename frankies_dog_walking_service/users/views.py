from django.shortcuts import render
from .models import  User, User_Appointment, Dog, Review
from walkers import models as walker_model
# Create your views here.



# index view
def index(request):
    list_of_walkers = walker_model.Walker.objects.all()
    ratings = walker_model.Review.objects.all()
    slots = walker_model.Walker_Appointment.objects.all()
    context = { 'list_of_walkers': list_of_walkers,
                'ratings': ratings,
                'slots': slots
            }
    return render(request, 'users/index.html', context)
