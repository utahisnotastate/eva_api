from django.contrib import admin
from .models import Patient, Provider, LatexAllergy, PollenAllergy, PetAllergies, DrugAllergies, FoodAllergies, InsectAllergies, Appointment, PatientRequest, PatientRequestUpdate, Demographics, Insurance, Address, Guarantor, ContactInformation, \
    PatientDocumentation, PatientReports, SurgicalHistory, Vital, Complaint, Assessment, Summary

# Register your models here.

admin.site.register(Patient)
admin.site.register(LatexAllergy)
admin.site.register(PollenAllergy)
admin.site.register(PetAllergies)
admin.site.register(DrugAllergies)
admin.site.register(FoodAllergies)
admin.site.register(InsectAllergies)
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
admin.site.register(Vital)
admin.site.register(Complaint)
admin.site.register(Assessment)
admin.site.register(Summary)

