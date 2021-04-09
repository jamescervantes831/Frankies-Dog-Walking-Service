from django.contrib import admin
from .models import Walker, Walker_Appointment, Review
# Register your models here.

admin.site.register(Walker)
admin.site.register(Walker_Appointment)
admin.site.register(Review)