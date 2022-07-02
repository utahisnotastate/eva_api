from django.contrib import admin
from .models import Patient, Provider, Appointment, Form, Request, Settings

# Register your models here.

admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Form)
admin.site.register(Request)
admin.site.register(Settings)




