from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


class Claim(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='claims')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='claims')


def default_form_details():
    return {
        "type": "",
        "value": "",
        "options": [],
        "typeField": "",
    }


def default_registration_form():
    return {
        "zone": "registration",
        "title": "Registration",
        "fields": []
    }


def default_physical_exam_form():
    return {
        "zone": "physical_exam",
        "title": "Physical Exam",
        "fields": []
    }


def default_review_of_systems_form():
    return {
        "zone": "review_of_systems",
        "title": "Review of Systems",
        "fields": []
    }


class Form(models.Model):
    zone = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    fields = ArrayField(
        JSONField(
            default=dict,
            blank=True,
        ),
        default=list,
        blank=True,
    )



class Settings(models.Model):
    name = models.CharField(max_length=500)
    details = JSONField(null=True)
    physical_exam_form = JSONField(default=default_physical_exam_form)
    review_of_systems_form = JSONField(default=default_review_of_systems_form)

class Provider(models.Model):
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    npi = models.CharField(max_length=100)


def default_appointment_details():
    return {
        "actual_start": "",
        "actual_end": "",
        "plans": [],
        "complaints": [],
        "assessments": [],
        "diagnoses": [],
        "followup": [],
        "summary": "",
        "physicalexam": [],
        "reviewofsystems": [],
    }


class ArtificialAIAppointment(models.Model):
    text = models.CharField(max_length=5000, blank=True, null=True)

class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='scheduled')
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    fields = ArrayField(
        JSONField(
            default=dict,
            blank=True,
        ),
        default=list,
        blank=True,
    )
    transcript = models.TextField(blank=True, null=True)
    complaints = ArrayField(JSONField(default=dict, blank=True), default=list, blank=True)
    review_of_systems = ArrayField(JSONField(default=dict, blank=True), default=list, blank=True)
    assessments = ArrayField(JSONField(default=dict, blank=True), default=list, blank=True)
    plans = ArrayField(JSONField(default=dict, blank=True), default=list, blank=True)
    physical_exam = ArrayField(JSONField(default=dict, blank=True), default=list, blank=True)
    summary = models.TextField(blank=True)


def default_patient_details():
    return {
        "demographics": {
            "first_name": "",
            "last_name": "",
            "address": "",
            "city": "",
            "state": "",
            "zip_code": "",
            "phone": "",
            "email": "",
            "date_of_birth": "",
        },
        "allergies": [],
        "insurance": [],
        "medications": [],
        "medical_history": [],
        "surgical_history": [],
    }


class Patient(models.Model):
    details = JSONField(default=default_patient_details)
    ssn = models.IntegerField(blank=False)
    fields = ArrayField(
        JSONField(
            default=dict,
            blank=True,
        ),
        default=list,
        blank=True,
    )

class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    fields = ArrayField(
        JSONField(
            default=dict,
            blank=True,
        ),
        default=list,
        blank=True,
    )


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
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    updates = ArrayField(
        JSONField(
            default=dict,
            blank=True,
        ),
        default=list,
        blank=True,
    )
