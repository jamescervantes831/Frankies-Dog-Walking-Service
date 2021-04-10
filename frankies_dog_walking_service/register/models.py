from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators
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