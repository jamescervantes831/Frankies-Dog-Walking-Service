from django.db import models
from django.core import validators
from users import models as user_model
from django.utils import timezone
# Create your models here.

class Walker(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        validators=[validators.EmailValidator()]
    )
    password = models.CharField(max_length=50)
    drop_off_point = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Walker_Appointment(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    appointment = models.DateTimeField(
        default=timezone.now, 
        auto_now = False, 
        auto_now_add= False
        )
    slots = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "I can only take 5 dogs at a time")]
        )
    
class Review(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    small_dog_rating = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "MAX RATING IS 5")]
        )
    medium_dog_rating = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "MAX RATING IS 5")]
        )
    large_dog_rating = models.IntegerField(
        default=0, 
        validators=[validators.MaxValueValidator(5, "MAX RATING IS 5")]
        )
