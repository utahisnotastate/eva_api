from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin
from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
appointments = router.register(r'appointments', views.AppointmentsViewSet)
forms = router.register(r'forms', views.FormViewSet)
# forms.register(r'formfields', views.FormFieldViewSet, basename='form-fields', parents_query_lookups=['form']).register(r'options', views.FormFieldOptionViewSet, basename='form-field-options', parents_query_lookups=['form_field_id', 'form_field'])
forms.register(r'formfields', views.FormFieldViewSet, basename='form-fields', parents_query_lookups=['form']).register(r'options', views.FormFieldOptionViewSet, basename='form-field-options', parents_query_lookups=['form_field_id', 'form_field'])
# appointments.register(r'today', views.TodaysAppointmentsViewSet, basename='todays-appointments', parents_query_lookups=['appointment'])
appointments.register(r'vitals', views.VitalViewSet, basename='appointment-vitals', parents_query_lookups=['appointment'])
appointments.register(r'complaints', views.ComplaintViewSet, basename='appointment-complaints', parents_query_lookups=['appointment'])
appointments.register(r'assessments', views.AssessmentViewSet, basename='appointment-assessments', parents_query_lookups=['appointment'])
appointments.register(r'findings', views.AppointmentFindingViewSet, basename='appointment-findings', parents_query_lookups=['appointment'])
appointments.register(r'summary', views.SummaryViewSet, basename='appointment-vitals', parents_query_lookups=['appointment'])

appointmentstoday = router.register(r'appointmentstoday', views.TodaysAppointmentsViewSet)

patients = router.register(r'patients', views.BasicPatientsViewSet)
patients.register(r'demographics', views.PatientDemographicsViewSet, basename='patient-demographics', parents_query_lookups=['patient'])
patients.register(r'address', views.PatientAddressViewSet, basename='patient-address', parents_query_lookups=['patient'])
patients.register(r'contactinformation', views.PatientContactInformationViewSet, basename='patient-contactinformation', parents_query_lookups=['patient'])
patients.register(r'guarantor', views.PatientGuarantorViewSet, basename='patient-guarantor', parents_query_lookups=['patient'])
patients.register(r'documents', views.PatientDocumentationViewSet, basename='patient-documents', parents_query_lookups=['patient'])
patients.register(r'reports', views.PatientReportViewSet, basename='patient-reports', parents_query_lookups=['patient'])
patients.register(r'surgicalhistory', views.PatientSurgicalHistoryViewSet, basename='surgical-history', parents_query_lookups=['patient'])

patients.register(r'patientrequests', views.PatientRequestsViewSet, basename='patient-requests', parents_query_lookups=['patient']).register(r'updates', views.PatientRequestsUpdateViewSet, basename='patient-request-updates', parents_query_lookups=['id', 'request_id'])
patients.register(r'createpatientrequest', views.CreatePatientRequestsViewSet, basename='create-patient-request', parents_query_lookups=['patient'])
patients.register(r'insurance', views.PatientInsurancesViewSet, basename='patient-insurances', parents_query_lookups=['patient'])
patients.register(r'appointments', views.AppointmentsViewSet, basename='patient-appointments', parents_query_lookups=['patient'])
patients.register(r'medications', views.PatientMedicationViewSet, basename='patient-medications', parents_query_lookups=['patient'])
patients.register(r'latexallergy', views.LatexAllergyViewSet, basename='patient-latexallergy', parents_query_lookups=['patient'])
patients.register(r'pollenallergy', views.PollenAllergyViewSet, basename='patient-pollenallergy', parents_query_lookups=['patient'])
patients.register(r'petallergy', views.PetAllergyViewSet, basename='patient-petallergy', parents_query_lookups=['patient'])
patients.register(r'drugallergy', views.DrugAllergyViewSet, basename='patient-drugallergy', parents_query_lookups=['patient'])
patients.register(r'foodallergy', views.FoodAllergyViewSet, basename='patient-foodallergy', parents_query_lookups=['patient'])
patients.register(r'insectallergy', views.InsectAllergyViewSet, basename='patient-insectallergy', parents_query_lookups=['patient'])

providers = router.register(r'providers', views.ProvidersViewSet)

clinicalrequests = router.register(r'clinicalrequests', views.PatientRequestsViewSet).register(r'updates', views.PatientRequestsUpdateViewSet, basename='clinical-request-updates', parents_query_lookups=['id', 'request_id'])


# urlpatterns = [
#     path('appointments/', views.AppointmentList.as_view()),
#     path('patient/<int:pk>/', views.BasicPatientDetail.as_view()),
#     path('patient/<int:pk>/demographics/', views.PatientDemographics.as_view()),
# ]
#.register(r'updates', views.PatientRequestsUpdateViewSet, basename='patient-request-updates', parents_query_lookups=['id', 'request_id'])
# , parents_query_lookups=['id', 'request_id']
