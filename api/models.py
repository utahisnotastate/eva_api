from django.contrib.postgres.fields import JSONField

# Create your models here.
from django.db import models

# Create your models here.

# User Models


class Claim(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='claims')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='claims')


def default_form_details():
    return {
        "fields": []
    }


class Form(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    details = JSONField(null=True, default=default_form_details)
    # location is where the form is used. eg. 'patient_profile'
    location = models.CharField(max_length=100, blank=True, null=True)


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
    # physical_exam_form = JSONField(null=True)
    physical_exam_form = JSONField(default=default_physical_exam_form)
    review_of_systems_form = JSONField(default=default_review_of_systems_form)


class Provider(models.Model):
    title_choices = [('Dr', 'Dr'), ('Nurse', 'Nurse')]
    title = models.CharField(choices=title_choices, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    npi = models.CharField(max_length=100)


def default_appointment_details():
    return {
        "status": "scheduled",
        "preappointmentnotes": "",
        "complaints": [],
        "assessments": [],
        "diagnoses": [],
        "followup": [],
        "summary": "",
        "physicalexam": [],
        "reviewofsystems": []
}
class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
    details = JSONField(default=default_appointment_details)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='scheduled')
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)


def default_patient_details():
    return {
        "familyhistory": [],
        "socialhistory": [],
        "medicalhistory": [],
        "surgicalhistory": [],
        "gender": "",
        "allergies": [],
        "diagnoses": [],
        "insurances": [],
        "medications": [],
        "first_name":"",
        "last_name" :"",
        "middle_name" :"",
        "preffered_name" :"",
        "address_one" :"",
        "address_two" :"",
        "city" :"",
        "state" :"",
        "zip" :"",
        "date_of_birth" :"",
        "contact_methods": [],
    }


class Patient(models.Model):
    details = JSONField(default=default_patient_details)
    ssn = models.IntegerField(blank=False)


class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    details = JSONField(null=True)


def default_request_details():
    return {
        "type": "",
        "description": "",
        "status": "",
        "date": "",
        "provider": "",
        "updates": []
    }


class Request(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='requests')
    details = JSONField(default=default_request_details)
