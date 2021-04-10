from django.db import models
from walkers import models as walker_model
from django.core import validators
from django.utils import timezone
from users import validations as v
import json

# Create your models here.



#Users model:
#   email, password, name, pick_up_address, date_joined
class User(models.Model):
    email = models.EmailField(
        verbose_name="email address",
        max_length=254,
        validators=[validators.EmailValidator()],
        unique=True
    )
    password= models.CharField(
        verbose_name="password",
        max_length=15,
        validators=[v.validate_password]
    )
    name= models.CharField(verbose_name="name", max_length=256)

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
    # True for pick_up_status, False  for drop_off_status
    pick_up = models.BooleanField(default=False)
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