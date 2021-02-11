from django.contrib import admin
from .models import Form,  Patient, Provider, Appointment, PatientRequest, PatientRequestUpdate, Demographics, Insurance, Address, Guarantor, ContactInformation, \
    PatientDocumentation, PatientReports, SurgicalHistory

# Register your models here.

admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Demographics)
admin.site.register(Insurance)
admin.site.register(Address)
admin.site.register(Guarantor)
admin.site.register(ContactInformation)
admin.site.register(PatientRequest)
admin.site.register(PatientRequestUpdate)
admin.site.register(PatientDocumentation)
admin.site.register(PatientReports)
admin.site.register(SurgicalHistory)
admin.site.register(Form)


