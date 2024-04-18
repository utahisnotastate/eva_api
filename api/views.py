from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from .helpers import call_openai_api
from .models import Provider, Appointment, Insurance, Patient, Settings, Request, ArtificialAIAppointment

from .serializers import InsuranceSerializer, SettingsSerializer, PatientSerializer, \
    BasicProviderSerializer, RequestSerializer, ProviderSerializer, AppointmentSerializer, \
    ArtificialAIAppointmentSerializer


class BasicProvidersViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = BasicProviderSerializer


# class AppointmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def handle_api_call(self, prompt_setup, text):
        """
        Helper function to handle API calls and check for errors.
        """
        result = call_openai_api(text, prompt_setup)
        if result.startswith("Error"):
            return None, result
        return result, None

    @action(methods=['post'], detail=False)
    def create_appointment(self, request):
        patient_id = request.data.get('patientId')
        if not patient_id:
            return Response({"error": "Patient ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate that the patient exists
        try:
            patient = Patient.objects.get(pk=patient_id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

        # Fetch default provider or handle if not existing
        try:
            default_provider = Provider.objects.first()  # Adjust if there's a specific provider to use
            if not default_provider:
                return Response({"error": "Default provider not found"}, status=status.HTTP_404_NOT_FOUND)
        except Provider.DoesNotExist:
            return Response({"error": "Provider data is corrupt"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            new_appointment = Appointment.objects.create(
                patient=patient,
                provider=default_provider,
                type='regular',
                status='scheduled',
                start=timezone.now(),
                end=None,  # Optional: Set if there's a default duration
                # Other fields can be set to defaults or left blank
            )
            return Response({"message": "Appointment created successfully", "appointmentId": new_appointment.id},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'])
    def clean_transcript(self, request, pk=None):
        appointment = self.get_object()
        prompt_setup = {
            "system_message": "The user is providing a rough audio transcript from a speech-to-text recording of a medical appointment for conversion into a clean, structured format suitable for an EMR (Electronic Medical Record) system. The task is to transform the provided text into a structured medical encounter transcript, which includes clear labels for the narrator/observer, doctor, patient, and any other participants, as well as a section for provider notes and follow-up recommendations."
        }
        cleaned_text, error = self.handle_api_call(prompt_setup, appointment.transcript)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        appointment.cleaneduptranscript = cleaned_text
        appointment.save()
        return Response({"message": "Transcript cleaned successfully", "cleaned_transcript": cleaned_text}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def generate_note(self, request, pk=None):
        appointment = self.get_object()
        prompt_setup = {
            "system_message": "Pretend you are a medical school professor who teaches clinical documentation. Please Generate a medical office note from the text given by the user which incorporates explaining the doctors logic, and everything from the audio transcript."
        }
        office_note, error = self.handle_api_call(prompt_setup, appointment.cleaneduptranscript)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        appointment.note = office_note
        appointment.save()
        return Response({"message": "Office note generated successfully", "office_note": office_note}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def generate_claim(self, request, pk=None):
        appointment = self.get_object()
        prompt_setup = {
            "system_message": "Pretend you are a medical billing/claims representative for the doctor's office. Please generate a claim from the provided medical appointment office note."
        }
        claim, error = self.handle_api_call(prompt_setup, appointment.note)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        appointment.claim = claim
        appointment.save()
        return Response({"message": "Claim generated successfully", "claim": claim}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def process_transcript(self, request, pk=None):
        appointment = self.get_object()
        response_data = {}

        # Step 1: Clean Transcript
        cleaned_transcript, error = self.handle_api_call({
            "system_message": "The user is providing a rough audio transcript for conversion into a clean, structured format suitable for an EMR."
        }, appointment.transcript)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_data['cleaned_transcript'] = cleaned_transcript
        appointment.cleaneduptranscript = cleaned_transcript

        # Step 2: Generate Office Note
        office_note, error = self.handle_api_call({
            "system_message": "Pretend you are a medical school professor teaching clinical documentation. Generate a medical office note."
        }, cleaned_transcript)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_data['office_note'] = office_note
        appointment.note = office_note

        # Step 3: Generate Claim
        claim, error = self.handle_api_call({
            "system_message": "Generate a claim from the medical office note as a claims representative."
        }, office_note)
        if error:
            return Response({"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_data['claim'] = claim
        appointment.claim = claim

        appointment.save()
        return Response(response_data, status=status.HTTP_200_OK)


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
