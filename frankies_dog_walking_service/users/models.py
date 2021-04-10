from django.db import models
from walkers import models as walker_model
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from users import validations as v
import json

# Create your models here.

#I thought I was creating a custom authentication and AuthO 
# and technically I did just not for the client side lol
class UserManager(BaseUserManager):
    def create_user(self,email, name, password=None):
        if not email:
            raise ValueError("email is required")
        if not password:
            raise ValueError("password is required")
        if not name:
            raise ValueError("name is required")
        user=self.model(
            email=self.normalize_email(email),
            password= password,
            name = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password=None):
        user=self.create_user(
            email = email,
            password = password,
            name = name
        )
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# Replacing default User class for Djangos admin auth and authO
class Super_User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=254,
        validators=[validators.EmailValidator()],
        unique=True
    )
    password = models.CharField(verbose_name="password", max_length=50)

    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =['password', 'pick_up_point']

    objects=UserManager();

    def __str__(self):
        return self.name
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

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