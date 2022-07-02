from django.contrib.postgres.fields import JSONField

# Create your models here.
from django.db import models


# Create your models here.

# User Models

class Claim(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='claims')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='claims')


class Form(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)
    details = JSONField(null=True)


# Appointment Models

def default_physical_exam_form():
    return {
        'title': 'Physical Exam',
        'description': 'Physical Exam',
        'fields': []
    }

def default_review_of_systems_form():
    return {
        'title': 'Review of Systems',
        'description': 'Review of Systems Form',
        'fields': []
    }

class Settings(models.Model):
    name = models.CharField(max_length=500)
    details = JSONField(null=True)
    #physical_exam_form = JSONField(null=True)
    physical_exam_form = JSONField(default=default_physical_exam_form)
    review_of_systems_form = JSONField(default=default_review_of_systems_form)


class Provider(models.Model):
    title_choices = [('Dr', 'Dr'), ('Nurse', 'Nurse')]
    title = models.CharField(choices=title_choices, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    npi = models.CharField(max_length=100)


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
    details = JSONField(null=True)
    type = models.CharField(max_length=100, blank=True, null=True)


"""
const details = {
    "familyhistory": [],
    "socialhistory": [],
    "medicalhistory": [],
    "surgicalhistory": [],
    "allergies": [],
    "requests": [],
    "diagnoses": [],
    "insurances": [],
    "medications": [],
    "appointments": [],
    "first_name" :"",
    "last_name" :"",
    "middle_name" :"",
    "preffered_name" :"",
    "address_one" :"",
    "address_two" :"",
    "city" :"",
    "state" :"",
    "zip" :"",
    "date_of_birth" :"",
    "contact_methods" :[],

}
"""

class Patient(models.Model):
    details = JSONField(null=True)
    ssn = models.IntegerField(blank=False)


class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    details = JSONField(null=True)


class Request(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='requests')
    details = JSONField(null=True)
