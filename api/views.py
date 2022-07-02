from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Provider, Appointment, Form, Insurance, Patient, Settings, Request
from .serializers import InsuranceSerializer, SettingsSerializer, FormSerializer, PatientSerializer, \
    BasicProviderSerializer, AppointmentSerializer, RequestSerializer, ProviderSerializer


class BasicProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = BasicProviderSerializer

class ProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class AppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



class FormsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer



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
