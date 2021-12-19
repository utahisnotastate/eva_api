from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import PracticeSettings, PracticeNews, Appointment, Allergy, PatientDiagnosis, PatientMedicationPrescription, PatientMedicationAuthorization,PatientMedicationHistory, PatientMedicationChanges, AppointmentForm, Patient, Provider, Demographics, Address, Guarantor, Insurance, ContactInformation, PatientRequest, PatientRequestUpdate, PatientDocumentation, PatientReports, SurgicalHistory, PatientMedication, Form


# Patient Serializers
"""
TODO Serializers:
- Claim
- Practice Settings
- Practice Update

"""
"""

"""
class PracticeSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeSettings
        fields = '__all__'

class PracticeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeNews
        fields = '__all__'


class BasicPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'ssn', 'preferred_name', 'display_name', 'date_of_birth')

class DemographicsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Demographics
        fields = ('race', 'gender', 'marital_status', 'employment_status', 'email')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_one', 'address_two', 'city', 'state', 'zip_code')


class PatientContactInformationSerializer(WritableNestedModelSerializer):
    number = PhoneNumberField()
    class Meta:
        model = ContactInformation
        # fields = ('patient', 'type', 'number', 'when_to_call', 'special_instructions')
        fields = ('id', 'type', 'number', 'special_instructions')


class PatientDiagnosisSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PatientDiagnosis
        fields = '__all__'

class PatientMedicationPrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationPrescription
        fields = "__all__"

class PatientMedicationAuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationAuthorization
        fields = '__all__'


class PatientMedicationSerializer(WritableNestedModelSerializer):
    # medication_diagnoses = PatientDiagnosisSerializer(many=True)
    prescriptions = PatientMedicationPrescriptionSerializer(many=True)
    medication_authorizations = PatientMedicationAuthorizationSerializer(many=True)

    class Meta:
        model = PatientMedication
        fields = '__all__'


class AppointmentSerializer(WritableNestedModelSerializer):
    patient_display_name = serializers.SerializerMethodField('get_patient_display_name')
    provider_display_name = serializers.SerializerMethodField('get_provider_display_name')
    clinical_data = serializers.JSONField()

    class Meta:
        model = Appointment
        fields = '__all__'

    def get_patient_display_name(self, appointment):
        patient_display_name = appointment.patient.display_name
        return patient_display_name

    def get_provider_display_name(self, appointment):
        provider_display_name = appointment.provider.display_name
        return provider_display_name

class ClinicalDataSerializer(WritableNestedModelSerializer):
    clinical_data = serializers.JSONField()

    class Meta:
        model = Appointment
        fields = ['clinical_data']

class PatientRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRequestUpdate
        # fields = ('id', 'request', 'update')
        fields = '__all__'


class PatientRequestsSerializer(WritableNestedModelSerializer):
    # patient = BasicPatientNameSerializer(read_only=True)
    patient_request_updates = PatientRequestUpdateSerializer(many=True)

    class Meta:
        model = PatientRequest
        #fields = ('id', 'patient', 'type', 'status', 'request_description', 'patient_request_updates')
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

class AllPatientInsurancesSerializer(WritableNestedModelSerializer):
    patient_insurances = InsuranceSerializer(many=True)
    class Meta:
        model = Patient
        fields = ['patient_insurances']


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'

class PatientSurgicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgicalHistory
        #fields = ('id', 'patient', 'procedure', 'date', 'performed_by', 'additional_information')
        fields = '__all__'

"""
  patient_medications = PatientMedicationSerializer(many=True)
    patient_contact_methods = PatientContactInformationSerializer(many=True)
    patient_diagnoses = PatientDiagnosisSerializer(many=True)
    appointments = Appoint mentSerializer(many=True)
    patient_requests = PatientRequestsSerializer(many=True)
    patient_insurances = PatientInsuranceSerializer(many=True)
    patient_allergies = AllergySerializer(many=True)
    patient_surgeries = PatientSurgicalHistorySerializer(many=True)
"""
class FullPatientSerializer(WritableNestedModelSerializer):
    patient_demographics = DemographicsSerializer()
    patient_address = AddressSerializer()
    patient_contact_methods = PatientContactInformationSerializer(many=True)
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'patient_demographics', 'patient_address', 'patient_contact_methods', 'last_name', 'middle_name', 'preferred_name', 'date_of_birth', 'ssn']

class BasicPatientNameSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'preferred_name', 'date_of_birth', 'ssn')
        #fields = ('id', 'first_name', 'last_name', 'middle_name', 'preferred_name', 'date_of_birth', 'ssn')


class BasicProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'display_name')

class AppointmentFormSerializer(serializers.ModelSerializer):
    form = serializers.JSONField()
    class Meta:
        model = AppointmentForm
        fields = '__all__'

class FormSerializer(WritableNestedModelSerializer):
    form = serializers.JSONField()

    class Meta:
        model = Form
        fields = '__all__'


class PatientMedicationPrescriptionHistorySerializer(WritableNestedModelSerializer):
    prescriptions = PatientMedicationPrescriptionSerializer(many=True)
    class Meta:
        model = PatientMedicationHistory
        fields = "__all__"

class BasicMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = ('id', 'strength', 'frequency','reason_stopped', 'name','active', 'requires_authorization', 'prescribed_by')



class PatientMedicationChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicationChanges
        fields = '__all__'


class PatientDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographics
        # fields = ('id', 'race', 'gender', 'marital_status', 'employment_status', 'email')
        fields = '__all__'

class PatientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        #fields = ('patient', 'active', 'address_one', 'address_two', 'city', 'state', 'zip_code')


class PatientGuarantorSerializer(serializers.ModelSerializer):
    patient = BasicPatientSerializer()

    class Meta:
        model = Guarantor
        fields = ('patient', 'relationship_to_patient', 'guarantor_first_name', 'guarantor_middle_name', 'guarantor_last_name',)





class PatientDocumentationSerializer(serializers.ModelSerializer):
    patient = BasicPatientSerializer()

    class Meta:
        model = PatientDocumentation
        fields = ('patient', 'file', 'description', 'uploaded_on')


class PatientReportsSerializer(serializers.ModelSerializer):
    patient = BasicPatientSerializer()

    class Meta:
        model = PatientReports
        fields = ('patient', 'type', 'file', 'received_on')







class CreatePatientRequestsSerializer(serializers.ModelSerializer):
    # patient = BasicPatientNameSerializer(read_only=True)
    # patient_request_updates = PatientRequestUpdateSerializer(many=True)

    class Meta:
        model = PatientRequest
        fields = ('patient', 'type', 'status', 'request_description')

"""
class LatexAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = LatexAllergy
        fields = ('patient', 'status')


class PollenAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = PollenAllergy
        fields = ('patient', 'status')


class PetAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = PetAllergies
        fields = ('patient', 'status')


class DrugAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugAllergies
        fields = ('patient', 'drug')


class FoodAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAllergies
        fields = ('patient', 'food')


class InsectAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsectAllergies
        fields = ('patient', 'insect')
"""

# Allergy Serializers
# Clinical Requests Serializers


# Appointment serializers

"""
class BasicAppointmentSerializer(serializers.ModelSerializer):
    patient_display_name = serializers.SerializerMethodField('get_patient_display_name')
    provider_display_name = serializers.SerializerMethodField('get_provider_display_name')
    # provider = BasicProviderSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'patient_display_name', 'provider', 'provider_display_name', 'type', 'status', 'start', 'end', 'scheduled_on', 'appointment_assessment', 'appointment_plan', 'appointment_summary')

    def get_patient_display_name(self, appointment):
        patient_display_name = appointment.patient.display_name
        return patient_display_name

    def get_provider_display_name(self, appointment):
        provider_display_name = appointment.provider.display_name
        return provider_display_name

"""
"""
class AppointmentVitalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vital
        fields = ('appointment', 'systolic_pressure', 'diastolic_pressure', 'temperature_value', 'temperature_unit', 'pulse', 'weight_value', 'weight_unit')

class AppointmentComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'appointment', 'complaint_name', 'complaint_description', 'location', 'onset_number',  'patient_belief_caused_by', 'patient_therapeutic_attempts', 'patients_guess', 'other_notes', 'appointment_complaints')
class ComplaintTherapeuticAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model: ComplaintTherapeuticAttempt
        fields = ('complaint', 'type', 'description', 'helped')

"""


"""
class AppointmentAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('appointment', 'icd_code', 'icd_description', 'other_assessment')



class AssessmentRelatedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentRelatedTo
        fields = ('assessment', 'category')



class AppointmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentPlan
        fields = '__all__'


class AppointmentSummarySerializer(serializers.ModelSerializer):
    appointment = BasicAppointmentSerializer()

    class Meta:
        model = Summary
        fields = 'summary'

"""







"""
class AppointmentFindingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentFinding
        fields = '__all__'
"""




# Form Serializers
"""
class FormFieldOptionSerializer(WritableNestedModelSerializer):

    class Meta:
        model = FormFieldOption
        fields = '__all__'


class FormFieldSerializer(WritableNestedModelSerializer):
    field_options = FormFieldOptionSerializer(many=True)

    class Meta:
        model = FormField
        fields = '__all__'

"""


