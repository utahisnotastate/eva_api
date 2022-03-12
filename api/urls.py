from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin, ExtendedDefaultRouter
from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()

appointments = router.register(r'appointments', views.AppointmentsViewSet)

forms = router.register(r'forms', views.FormsViewSet)
appointmentstoday = router.register(r'appointmentstoday', views.TodaysAppointmentsViewSet, basename='appointments-today')

patients = router.register(r'patients', views.PatientViewSet)

patients.register(r'medications', views.PatientMedicationViewSet, 'patient-basic-medications', parents_query_lookups=['patient'])
patients.register(r'patientrequests', views.PatientRequestsViewSet, basename='patient-requests', parents_query_lookups=['patient']).register(r'updates', views.PatientRequestsUpdateViewSet, basename='patient-request-updates', parents_query_lookups=['id', 'request_id'])
patients.register(r'createpatientrequest', views.CreatePatientRequestsViewSet, basename='create-patient-request', parents_query_lookups=['patient'])
patients.register(r'patient_insurances', views.PatientInsurancesViewSet, basename='patient-insurances', parents_query_lookups=['patient'])
patients.register(r'appointments', views.AppointmentsViewSet, basename='patient-appointments', parents_query_lookups=['patient'])
patients.register(r'medications', views.PatientMedicationViewSet, basename='patient-medications', parents_query_lookups=['patient'])
clinicalrequests = router.register(r'clinicalrequests', views.PatientRequestsViewSet).register(r'updates', views.PatientRequestsUpdateViewSet, basename='clinical-request-updates', parents_query_lookups=['id', 'request_id'])
providers = router.register(r'providers', views.BasicProvidersViewSet)

