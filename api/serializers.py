from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Appointment,  Patient, Provider, Insurance, Form,  Claim, Settings, Request


# Patient Serializers
"""
TODO Serializers:
- Claim
- Practice Settings
- Practice Update

"""
"""

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

class FormSerializer(WritableNestedModelSerializer):
    details = serializers.JSONField()
    class Meta:
        model = Form
        fields = '__all__'

class PatientSerializer(WritableNestedModelSerializer):

    details = serializers.JSONField()
    class Meta:
        model = Patient
        fields = '__all__'
        label: 'Patient'

class AppointmentSerializer(WritableNestedModelSerializer):
    patient = PatientSerializer(read_only=True)
    details = serializers.JSONField()

    class Meta:
        model = Appointment
        fields = '__all__'




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
    patient = PatientSerializer(read_only=True)   # get details.first_name and details.last_name from Patient Serializer
    class Meta:
        model = Request
        fields = '__all__'
