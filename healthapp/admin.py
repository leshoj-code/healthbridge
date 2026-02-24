from django.contrib import admin

from healthapp.models import Patient

from healthapp.models import Myappointment

# Register your models here.
admin.site.register(Patient)

admin.site.register(Myappointment)