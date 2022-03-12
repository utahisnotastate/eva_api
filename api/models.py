from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

# User Models

class Claim(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='claims')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='claims')
    guarantor = models.ForeignKey('Guarantor', on_delete=models.CASCADE)


class Form(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)
    details = JSONField(null=True)
# Appointment Models


class Settings(models.Model):
    name = models.CharField(max_length=500)
    details = JSONField(null=True)

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



class Patient(models.Model):
    details = JSONField(null=True)
    ssn = models.IntegerField(blank=False)


class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    details = JSONField(null=True)


class Request(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='requests')
    details = JSONField(null=True)

