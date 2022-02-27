from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin, ExtendedDefaultRouter
from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
practice_settings = router.register(r'practice_settings', views.PracticeSettingsViewSet)
practice_news = router.register(r'practice_news', views.PracticeNewsViewSet)

appointments = router.register(r'appointments', views.AppointmentsViewSet)

forms = router.register(r'forms', views.FormsViewSet)
appointmentstoday = router.register(r'appointmentstoday', views.TodaysAppointmentsViewSet, basename='appointments-today')

#patients = router.register(r'patients', views.FullPatientsViewSet)
patients = router.register(r'patients', views.PatientViewSet)

patients.register(r'medications', views.PatientMedicationViewSet, 'patient-basic-medications', parents_query_lookups=['patient'])
patients.register(r'patientrequests', views.PatientRequestsViewSet, basename='patient-requests', parents_query_lookups=['patient']).register(r'updates', views.PatientRequestsUpdateViewSet, basename='patient-request-updates', parents_query_lookups=['id', 'request_id'])
patients.register(r'createpatientrequest', views.CreatePatientRequestsViewSet, basename='create-patient-request', parents_query_lookups=['patient'])
patients.register(r'patient_insurances', views.PatientInsurancesViewSet, basename='patient-insurances', parents_query_lookups=['patient'])
patients.register(r'appointments', views.AppointmentsViewSet, basename='patient-appointments', parents_query_lookups=['patient'])
patients.register(r'medications', views.PatientMedicationViewSet, basename='patient-medications', parents_query_lookups=['patient'])
clinicalrequests = router.register(r'clinicalrequests', views.PatientRequestsViewSet).register(r'updates', views.PatientRequestsUpdateViewSet, basename='clinical-request-updates', parents_query_lookups=['id', 'request_id'])
providers = router.register(r'providers', views.BasicProvidersViewSet)

"""
appointments.register(r'vitals', views.VitalViewSet, basename='appointment-vitals', parents_query_lookups=['appointment'])
appointments.register(r'complaints', views.ComplaintViewSet, basename='appointment-complaints', parents_query_lookups=['appointment'])
appointments.register(r'forms', views.AppointmentFormViewSet, basename='appointment-forms', parents_query_lookups=['appointment']).register(r'findings', views.AppointmentFindingViewSet, basename='appointment-findings', parents_query_lookups=['appointment', 'id'])
appointments.register(r'assessments', views.AssessmentViewSet, basename='appointment-assessments', parents_query_lookups=['appointment'])
appointments.register(r'findings', views.AppointmentFindingViewSet, basename='appointment-findings', parents_query_lookups=['appointment'])
appointments.register(r'summary', views.SummaryViewSet, basename='appointment-vitals', parents_query_lookups=['appointment'])
"""
#patients.register(r'allergies', views.PatientAllergyViewSet, basename='patient-allergies', parents_query_lookups=['patient'])

#patient_medications.register(r'prescriptions', views.PatientMedicationPrescriptionViewSet, basename='medication-prescriptions', parents_query_lookups=['id', 'medication'])
#patient_medications.register(r'authorizations', views.PatientMedicationAuthorizationViewSet, basename='patient-medication-authorizations', parents_query_lookups=['medication_id', 'id'])
#patients.register(r'basicmedications', views.BasicPatientMedicatonViewSet, 'patient-basic-medications', parents_query_lookups=['patient'])



#patients.register(r'medications', views.PatientMedicationViewSet, basename='patient-medications', parents_query_lookups=['patient']).register(r'prescriptions', views.PatientMedicationPrescriptionViewSet, basename='medication-prescriptions', parents_query_lookups=['id', 'medication_id'])
"""
patients.register(r'latexallergy', views.LatexAllergyViewSet, basename='patient-latexallergy', parents_query_lookups=['patient'])
patients.register(r'pollenallergy', views.PollenAllergyViewSet, basename='patient-pollenallergy', parents_query_lookups=['patient'])
patients.register(r'petallergy', views.PetAllergyViewSet, basename='patient-petallergy', parents_query_lookups=['patient'])
patients.register(r'drugallergy', views.DrugAllergyViewSet, basename='patient-drugallergy', parents_query_lookups=['patient'])
patients.register(r'foodallergy', views.FoodAllergyViewSet, basename='patient-foodallergy', parents_query_lookups=['patient'])
patients.register(r'insectallergy', views.InsectAllergyViewSet, basename='patient-insectallergy', parents_query_lookups=['patient'])
"""


#activeforms = router.register(r'activeforms', views.ActiveFormsViewSet, basename='activeforms')
#activephysicalexamforms = router.register(r'activephysicalexamforms', views.ActivePhysicalExamFormsViewSet, basename='active-physical-exam-forms')
#activerosforms = router.register(r'activerosforms', views.ActiveROSFormsViewSet, basename='active-ros-forms')
# forms.register(r'formfields', views.FormFieldViewSet, basename='form-fields', parents_query_lookups=['form']).register(r'options', views.FormFieldOptionViewSet, basename='form-field-options', parents_query_lookups=['form_field_id', 'form_field'])
#forms.register(r'formfields', views.FormFieldViewSet, basename='form-fields', parents_query_lookups=['form']).register(r'options', views.FormFieldOptionViewSet, basename='form-field-options', parents_query_lookups=['form_field_id', 'form_field'])
# appointments.register(r'today', views.TodaysAppointmentsViewSet, basename='todays-appointments', parents_query_lookups=['appointment'])


#patients = router.register(r'patients', views.BasicPatientsViewSet)
# patients = router.register(r'patients', views.FullPatientsViewSet)
# patients.register(r'basicinfo', views.BasicPatientsViewSet, basename='patients-basicinfo', parents_query_lookups=['id'])
#patients.register(r'demographics', views.PatientDemographicsViewSet, basename='patient-demographics', parents_query_lookups=['patient'])
#patients.register(r'address', views.PatientAddressViewSet, basename='patient-address', parents_query_lookups=['patient'])
#patients.register(r'contactinformation', views.PatientContactInformationViewSet, basename='patient-contactinformation', parents_query_lookups=['patient'])
#patients.register(r'guarantor', views.PatientGuarantorViewSet, basename='patient-guarantor', parents_query_lookups=['patient'])
#patients.register(r'documents', views.PatientDocumentationViewSet, basename='patient-documents', parents_query_lookups=['patient'])
#patients.register(r'reports', views.PatientReportViewSet, basename='patient-reports', parents_query_lookups=['patient'])
#patients.register(r'surgicalhistory', views.PatientSurgicalHistoryViewSet, basename='surgical-history', parents_query_lookups=['patient'])
#patients.register(r'diagnoses', views.PatientDiagnosisViewSet, basename='patient-diagnoses', parents_query_lookups=['patient'])
#patients.register(r'medications', views.PatientMedicationViewSet, basename='medications', parents_query_lookups=['patient'])
#patient_medications.register(r'changes', views.PatientMedicationChangesViewSet, basename='patient_medication-changes', parents_query_lookups=['id', 'medication_id'])
#patient_medications.register(r'prescriptions', views.PatientMedicationPrescriptionViewSet, basename='patient_medication-prescriptions', parents_query_lookups=['id', 'medication_id'])
#patient_medications.register(r'diagnoses', views.PatientMedicationViewSet, basename='patient_medication-diagnoses', parents_query_lookups=['id', 'medication_diagnoses'])
#patient_medications.register(r'diagnoses', views.PatientMedicationViewSet, basename='diagnoses_medication', parents_query_lookups=['patient', 'medication_diagnoses'])
#patient_medications.register(r'changes')


# urlpatterns = [
#     path('appointments/', views.AppointmentList.as_view()),
#     path('patient/<int:pk>/', views.BasicPatientDetail.as_view()),
#     path('patient/<int:pk>/demographics/', views.PatientDemographics.as_view()),
# ]
#.register(r'updates', views.PatientRequestsUpdateViewSet, basename='patient-request-updates', parents_query_lookups=['id', 'request_id'])
# , parents_query_lookups=['id', 'request_id']
