from django.contrib import admin
from .models import Patient, Provider, Appointment, PatientRequest, PatientRequestUpdate, Insurance, Guarantor

# Register your models here.

admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Insurance)
admin.site.register(Guarantor)
admin.site.register(PatientRequest)


