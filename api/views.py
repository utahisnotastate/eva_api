from rest_framework import generics, viewsets, filters
import datetime
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import PracticeSettings, PracticeNews, Provider, Appointment, AppointmentForm,  Form, Allergy, PatientDiagnosis, PatientMedicationChanges,PatientMedicationAuthorization ,PatientMedicationPrescription, Insurance, Patient, Demographics, Address, Guarantor, PatientDocumentation, PatientReports, SurgicalHistory, PatientMedication, PatientRequest, PatientRequestUpdate, ContactInformation
from .serializers import PracticeSettingsSerializer,InsuranceSerializer, AllPatientInsurancesSerializer, BasicPatientNameSerializer, PracticeNewsSerializer, AppointmentSerializer, BasicProviderSerializer, AppointmentSerializer, AppointmentFormSerializer, FormSerializer, AllergySerializer, BasicMedicationSerializer,PatientMedicationChangesSerializer,PatientMedicationAuthorizationSerializer, PatientMedicationPrescriptionHistorySerializer,PatientMedicationPrescriptionSerializer, PatientDiagnosisSerializer, CreatePatientRequestsSerializer, PatientInsuranceSerializer, PatientRequestUpdateSerializer, PatientRequestsSerializer,  BasicPatientSerializer, FullPatientSerializer, PatientDemographicsSerializer, PatientAddressSerializer, PatientGuarantorSerializer, PatientDocumentationSerializer, PatientReportsSerializer, PatientSurgicalHistorySerializer, PatientMedicationSerializer, PatientContactInformationSerializer
from django.shortcuts import render

# Create your views here.
class PracticeSettingsViewSet(viewsets.ModelViewSet):
    queryset = PracticeSettings.objects.all()
    serializer_class = PracticeSettingsSerializer

class PracticeNewsViewSet(viewsets.ModelViewSet):
    queryset = PracticeNews.objects.all()
    serializer_class = PracticeNewsSerializer

class BasicProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = BasicProviderSerializer

class AppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentFormViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AppointmentForm.objects.all()
    serializer_class = AppointmentFormSerializer


class FormViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class ActiveFormsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Form.objects.filter(active=True)
    serializer_class = FormSerializer

class ActivePhysicalExamFormsViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.filter(form_type='physical_exam', active=True)
    serializer_class = FormSerializer

class ActiveROSFormsViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.filter(form_type='review_of_systems', active=True)
    serializer_class = FormSerializer
"""
class FormFieldViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer

class FormFieldOptionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = FormFieldOption.objects.all()
    serializer_class = FormFieldOptionSerializer
"""


"""
class AppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = BasicAppointmentSerializer
"""
#queryset = AppointmentForm.objects.filter(form__values__contains={'checked': True})
#serializer_class = AppointmentFindingsSerializer
#queryset = AppointmentForm.objects.filter(form__customformfields__contains=[{'checked': True}])
#queryset = AppointmentForm.objects.filter(form__customformfields__contains=[{'checked': True}])
#queryset = AppointmentForm.objects.filter(form__customformfields__contains={'checked': True})

"""
"""
class AppointmentFindingViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AppointmentForm.objects.filter(form__customformfields__contains=[{'checked': True}])
    serializer_class = AppointmentFormSerializer

class TodaysAppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.filter(start__date=datetime.date.today())
    serializer_class = AppointmentSerializer


class PatientInsurancesViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
# Patient View Sets

class CreatePatientRequestsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientRequest.objects.all()
    serializer_class = CreatePatientRequestsSerializer


class PatientRequestsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientRequest.objects.all()
    serializer_class = PatientRequestsSerializer


class PatientDiagnosisViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer


class PatientRequestsUpdateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientRequestUpdate.objects.all()
    serializer_class = PatientRequestUpdateSerializer


class PatientContactInformationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = PatientContactInformationSerializer


class PatientMedicationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer


class PatientMedicationAuthorizationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientMedicationAuthorization.objects.all()
    serializer_class = PatientMedicationAuthorizationSerializer


class BasicPatientMedicatonViewSet(viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = BasicMedicationSerializer



class PatientMedicationChangesViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientMedicationChanges.objects.all()
    serializer_class = PatientMedicationChangesSerializer

class PatientMedicationPrescriptionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientMedicationPrescription.objects.all()
    serializer_class = PatientMedicationPrescriptionSerializer


class PatientDemographicsViewSet(viewsets.ModelViewSet):
    queryset = Demographics.objects.all()
    serializer_class = PatientDemographicsSerializer


class PatientAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = PatientAddressSerializer


class PatientGuarantorViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = PatientGuarantorSerializer


class PatientDocumentationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientDocumentation.objects.all()
    serializer_class = PatientDocumentationSerializer


class PatientReportViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PatientReports.objects.all()
    serializer_class = PatientReportsSerializer


class PatientSurgicalHistoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = SurgicalHistory.objects.all()
    serializer_class = PatientSurgicalHistorySerializer

"""
class BasicPatientsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = BasicPatientNameSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'last_name', 'middle_name', 'preferred_name', 'date_of_birth']
"""


class BasicPatientsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = BasicPatientNameSerializer

class FullPatientsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = FullPatientSerializer

class PatientAllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
"""
class VitalViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = AppointmentVitalsSerializer
class ComplaintViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = AppointmentComplaintSerializer


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AppointmentAssessmentSerializer


class SummaryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = AppointmentSummarySerializer    
"""

"""
#Allergy View Sets
class LatexAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = LatexAllergy.objects.all()
    serializer_class = LatexAllergySerializer


class PollenAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PollenAllergy.objects.all()
    serializer_class = PollenAllergySerializer


class PetAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PetAllergies.objects.all()
    serializer_class = PetAllergySerializer


class DrugAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DrugAllergies.objects.all()
    serializer_class = DrugAllergySerializer


class FoodAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = FoodAllergies.objects.all()
    serializer_class = FoodAllergySerializer


class InsectAllergyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = InsectAllergies.objects.all()
    serializer_class = InsectAllergySerializer
"""

