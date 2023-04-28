from django.contrib import admin
from .models import Service, Appointment, Feedback

# Register your models here.

admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Feedback)