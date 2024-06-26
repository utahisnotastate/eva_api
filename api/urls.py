from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin, ExtendedDefaultRouter
from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

#create nested route for patients which shows the appointments for that patient
appointments = router.register(r'appointments', views.AppointmentViewSet)
artificalaiappointment = router.register(r'artificalaiappointment', views.ArtificalAIAppointmentViewSet)
settings = router.register(r'settings', views.SettingsViewSet)
patients = router.register(r'patients', views.PatientViewSet)
patients.register(r'appointments', views.AppointmentViewSet, basename='patient-appointments', parents_query_lookups=['patient'])
requests = router.register(r'requests', views.RequestViewSet)
providers = router.register(r'providers', views.ProvidersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]