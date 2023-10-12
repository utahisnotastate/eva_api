from django.contrib import admin
from django.contrib.postgres.forms import SimpleArrayField
from django.forms import Textarea
from .models import Provider, Appointment, Form, Request, Settings, Patient, Provider


admin.site.register(Appointment)
admin.site.register(Request)
admin.site.register(Form)
admin.site.register(Provider)
admin.site.register(Settings)
admin.site.register(Patient)

