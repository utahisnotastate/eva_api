from rest_framework import generics, viewsets, filters
import datetime
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import  Provider, Appointment,Form, Insurance, Patient
from .serializers import InsuranceSerializer, FormSerializer, PatientSerializer,  AppointmentSerializer, BasicProviderSerializer, AppointmentSerializer, PatientInsuranceSerializer
from django.shortcuts import render


class BasicProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = BasicProviderSerializer

class AppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



class FormsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


class TodaysAppointmentsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appointment.objects.filter(start__date=datetime.date.today())
    serializer_class = AppointmentSerializer


class PatientViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientInsurancesViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
# Patient View Sets


