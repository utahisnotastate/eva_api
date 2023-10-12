from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Provider, Appointment, Insurance, Patient, Settings, Request, ArtificialAIAppointment

from .serializers import InsuranceSerializer, SettingsSerializer, PatientSerializer, \
    BasicProviderSerializer, RequestSerializer, ProviderSerializer, AppointmentSerializer, ArtificialAIAppointmentSerializer

class BasicProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = BasicProviderSerializer

class AppointmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ArtificalAIAppointmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ArtificialAIAppointment.objects.all()
    serializer_class = ArtificialAIAppointmentSerializer

class ProvidersViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class PatientViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class SettingsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class PatientInsurancesViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class RequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
