from django.contrib import admin
from .models  import User, User_Appointment, Dog, Review
# Register your models here.




admin.site.register(User)
admin.site.register(User_Appointment)
admin.site.register(Dog)
admin.site.register(Review)