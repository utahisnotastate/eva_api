from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Appointment,  Patient, Provider, Insurance, Form,  Claim


# Patient Serializers
"""
TODO Serializers:
- Claim
- Practice Settings
- Practice Update

"""
"""

"""


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

class AppointmentSerializer(WritableNestedModelSerializer):
    patient_display_name = serializers.SerializerMethodField('get_patient_display_name')
    provider_display_name = serializers.SerializerMethodField('get_provider_display_name')
    details = serializers.JSONField()

    class Meta:
        model = Appointment
        fields = '__all__'

    def get_patient_display_name(self, appointment):
        patient_display_name = appointment.patient.display_name
        return patient_display_name

    def get_provider_display_name(self, appointment):
        provider_display_name = appointment.provider.display_name
        return provider_display_name


class PatientSerializer(WritableNestedModelSerializer):
    details = serializers.JSONField()
    class Meta:
        model = Patient
        fields = '__all__'



class PatientInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        #fields = ('id', 'patient', 'insurance_name', 'tradingPartnerId', 'group_ID', 'bin_number', 'pcn', 'type', 'member_id','relationship_code', 'active', 'date_effective', 'date_terminated', 'copay_amount')
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'
