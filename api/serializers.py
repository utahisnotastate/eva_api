from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Appointment,  Patient, Provider, Insurance, Form,  Claim, Settings, Request


"""
TODO Serializers:
- Claim
- Practice Settings
- Practice Update
"""

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class BasicProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'display_name')

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = '__all__'

class PatientSerializer(WritableNestedModelSerializer):
    fields = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(),
            help_text='A dictionary of properties for the field.',
            label='Field Properties',
        ),
    )
    class Meta:
        model = Patient
        fields = '__all__'
        label: 'Patient'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'provider',
            'details',
            'type',
            'status',
            'start',
            'end',
            'fields',
            'complaints',
            'review_of_systems',
            'assessments',
            'plans',
            'physical_exam',
            'summary',
        ]

class PatientInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    details = serializers.JSONField()
    class Meta:
        model = Insurance
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
   updates =  serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(),
            help_text='A dictionary of properties for the field.',
            label='Field Properties',
        ),
    )
   class Meta:
        model = Request
        fields = '__all__'
