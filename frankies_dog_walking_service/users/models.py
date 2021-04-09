from django.db import models
from walkers import models as walker_model
from django.core import validators
from django.utils import timezone
import json
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        validators=[validators.EmailValidator()]
    )
    password = models.CharField(max_length=50)
    pick_up_point = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User_Appointment(models.Model):
    walker = models.ForeignKey(
        walker_model.Walker, 
    on_delete=models.CASCADE
    )
    appointment = models.DateTimeField(
        default=timezone.now, 
        auto_now = False, auto_now_add= False
        )
    slots = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "I can only take 5 dogs at a time")]
        )

class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dog_type = models.CharField(
        max_length= 15,
        default="Pick the breed of your dog"
    )
    SMALL="SM"
    MEDIUM="MD"
    LARGE="LG"
    DOG_SIZE = [
        (SMALL,'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large')
    ]
    dog_size = models.CharField(
        max_length=7,
        choices=DOG_SIZE,
        default=DOG_SIZE[0]  
    )
    def __str__(self):
        return self.name

class Review(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    review = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "MAX RATING IS 5")]
        )