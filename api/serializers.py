from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Appointment, AppointmentFinding, AppointmentForm, LatexAllergy, PollenAllergy, PetAllergies, DrugAllergies, FoodAllergies, InsectAllergies, Patient, Provider, Demographics, Address, Guarantor, Insurance, ContactInformation, PatientRequest, PatientRequestUpdate, PatientDocumentation, PatientReports, SurgicalHistory, PatientMedication, Vital, Complaint, ComplaintTherapeuticAttempt, Assessment, AssessmentRelatedTo, AppointmentPlan,  Summary, Form, FormField, FormFieldOption


# Patient Serializers

class BasicPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'ssn', 'preferred_name', 'display_name', 'date_of_birth')


class BasicPatientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'preferred_name', 'display_name', 'date_of_birth')


class BasicProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'display_name')


class PatientMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = ('id', 'patient', 'last_written_on', 'prescribed_by', 'diagnosis', 'name', 'date_started', 'date_stopped', 'stoppage_reason', 'dosage', 'dosage_unit', 'frequency')



class PatientInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ('id', 'patient', 'insurance_name', 'tradingPartnerId', 'group_ID', 'bin_number', 'pcn', 'type', 'member_id','relationship_code', 'active', 'date_effective', 'date_terminated', 'copay_amount')


class PatientDemographicsSerializer(serializers.ModelSerializer):
     #patient = BasicPatientSerializer()

    class Meta:
        model = Demographics
        fields = ('patient', 'race', 'gender', 'marital_status', 'employment_status', 'email')


class PatientAddressSerializer(serializers.ModelSerializer):
    # patient = BasicPatientSerializer()

    class Meta:
        model = Address
        fields = ('patient', 'active', 'address_one', 'address_two', 'city', 'state', 'zip_code')


class PatientGuarantorSerializer(serializers.ModelSerializer):
    patient = BasicPatientSerializer()

    class Meta:
        model = Guarantor
        fields = ('patient', 'relationship_to_patient', 'guarantor_first_name', 'guarantor_middle_name', 'guarantor_last_name',)


class PatientContactInformationSerializer(serializers.ModelSerializer):
    #patient = BasicPatientSerializer()

    class Meta:
        model = ContactInformation
        fields = ('patient', 'type', 'number', 'when_to_call', 'special_instructions')


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


class PatientSurgicalHistorySerializer(serializers.ModelSerializer):
    # patient = BasicPatientSerializer()

    class Meta:
        model = SurgicalHistory
        fields = ('id', 'patient', 'procedure', 'date', 'performed_by', 'additional_information')


class PatientRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRequestUpdate
        fields = ('id', 'request', 'update')


class CreatePatientRequestsSerializer(serializers.ModelSerializer):
    # patient = BasicPatientNameSerializer(read_only=True)
    # patient_request_updates = PatientRequestUpdateSerializer(many=True)

    class Meta:
        model = PatientRequest
        fields = ('patient', 'type', 'status', 'request_description')


class PatientRequestsSerializer(serializers.ModelSerializer):
    # patient = BasicPatientNameSerializer(read_only=True)
    patient_request_updates = PatientRequestUpdateSerializer(many=True, read_only=True)

    class Meta:
        model = PatientRequest
        fields = ('id', 'patient', 'type', 'status', 'request_description', 'patient_request_updates')

# Allergy Serializers


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

# Clinical Requests Serializers


# Appointment serializers
class BasicAppointmentSerializer(serializers.ModelSerializer):
    patient_display_name = serializers.SerializerMethodField('get_patient_display_name')
    provider_display_name = serializers.SerializerMethodField('get_provider_display_name')
    # provider = BasicProviderSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'patient_display_name', 'provider', 'provider_display_name', 'type', 'status', 'start', 'end', 'scheduled_on')

    def get_patient_display_name(self, appointment):
        patient_display_name = appointment.patient.display_name
        return patient_display_name

    def get_provider_display_name(self, appointment):
        provider_display_name = appointment.provider.display_name
        return provider_display_name


class AppointmentVitalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vital
        fields = ('appointment', 'systolic_pressure', 'diastolic_pressure', 'temperature_value', 'temperature_unit', 'pulse', 'weight_value', 'weight_unit')


class AppointmentComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'appointment', 'complaint_name', 'complaint_description', 'location', 'onset_number',  'patient_belief_caused_by', 'patient_therapeutic_attempts', 'patients_guess', 'other_notes')

class ComplaintTherapeuticAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model: ComplaintTherapeuticAttempt
        fields = ('complaint', 'type', 'description', 'helped')


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

class AppointmentFormSerializer(serializers.ModelSerializer):
    #title = serializers.SerializerMethodField('get_form_title')

    class Meta:
        model = AppointmentForm
        fields = '__all__'

    #def get_form_title(self, appointmentform):
        #title = appointmentform.form.title
       # return title


class AppointmentFindingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentFinding
        fields = '__all__'



# Form Serializers


class FormFieldOptionSerializer(WritableNestedModelSerializer):

    class Meta:
        model = FormFieldOption
        fields = '__all__'


class FormFieldSerializer(WritableNestedModelSerializer):
    field_options = FormFieldOptionSerializer(many=True)

    class Meta:
        model = FormField
        fields = '__all__'


class FormSerializer(WritableNestedModelSerializer):
    #form_fields = FormFieldSerializer(many=True)

    class Meta:
        model = Form
        fields = '__all__'

