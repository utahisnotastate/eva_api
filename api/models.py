from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

# User Models

class Claim(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='claims')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='claims')
    guarantor = models.ForeignKey('Guarantor', on_delete=models.CASCADE)


"""
form details object looks like this
{
fields: [],

}

"""

class Form(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    details = JSONField(null=True)


# Appointment Models




class PracticeSettings(models.Model):
    name = models.CharField(max_length=500)
    address_one = models.CharField(max_length=500)
    address_two = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=12)
    npi = models.CharField(max_length=100)
    first_appointment_starts = models.TimeField()
    last_appointment_ends = models.TimeField()
    close = models.TimeField()
    tax_id = models.CharField(max_length=100)
    phone_number = PhoneNumberField()


class PracticeNews(models.Model):
    title = models.TextField(blank=True)
    news =  models.TextField(blank=True)
    display = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)


class Provider(models.Model):
    title_choices = [('Dr', 'Dr'), ('Nurse', 'Nurse')]
    title = models.CharField(choices=title_choices, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    npi = models.CharField(max_length=100)

    @property
    def display_name(self):
        return '%s %s' % (self.title, self.last_name)

    def __str__(self):
        return '%s %s' % (self.title, self.last_name)



"""
encounter should be: 
{
    complaints: [],
    physical_exam_forms: [],
    review_of_systems: [],
    assessments: [],
    plans: [],
    summary: ""
    follow_up: []
}
    
}
"""


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
    type = models.CharField(max_length=100, blank=True, null=True)
    encounter = JSONField(null=True)
    status = models.CharField(max_length=100, default="scheduled")
    start = models.DateTimeField()
    actual_start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField()
    actual_end = models.DateTimeField(blank=True, null=True)
    scheduled_on = models.DateTimeField(auto_now_add=True)
    scheduling_note = models.TextField(blank=True, null=True)



# Patient Models

"""
MEDICATION DETAILS PROP
{
    prescription_history: [],
    authorizations: [],
    diagnoses: [],
    
}

"""



class PatientMedication(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_medications')
    #diagnosis = models.ForeignKey(PatientDiagnosis, on_delete=models.CASCADE,
    #                             related_name='patient_medications_for_diagnosis', blank=True, null=True)
    #prescribed_by = models.CharField(max_length=300, blank=True, null=True)
    prescribed_by = models.CharField(max_length=300, blank=True)
    details = JSONField(null=True)
    requires_authorization = models.BooleanField(null=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    strength = models.CharField(max_length=100, blank=True)
    #dosage_unit = models.CharField(max_length=100)
    frequency = models.CharField(max_length=400, blank=True)
    reason_stopped = models.TextField(blank=True)
    #date_started = models.DateField(blank=True, null=True)
    #date_stopped = models.DateField(blank=True, null=True)
    #stoppage_reason = models.TextField(blank=True, null=True)
    # diagnosis = models.TextField()
    #diagnosis = models.ManyToManyField(PatientDiagnosis, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.strength)

class PatientDiagnosis(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_diagnoses')
    diagnosis_icd_code = models.CharField(max_length=200, blank=True)
    diagnosis_description = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=100, blank=True)
    diagnosed_on = models.DateField(blank=True, null=True)
    diagnosed_by = models.CharField(max_length=200, blank=True)
    medications = models.ManyToManyField(PatientMedication, blank=True, related_name="diagnosis_medications")

    def __str__(self):
        return '%s %s' % (self.diagnosis_icd_code, self.diagnosis_description)




class PatientMedicationPrescription(models.Model):
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE,
                                   related_name='prescriptions')
    strength = models.CharField(max_length=200, blank=True)
    frequency = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    refills = models.SmallIntegerField(blank=True, null=True)
    written_on = models.DateField(auto_now_add=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='medications_written_by')



class PatientMedicationChanges(models.Model):
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE,
                                   related_name='patient_medication_changes')
    new_strength = models.CharField(max_length=200, blank=True)
    new_frequency = models.CharField(max_length=200, blank=True)
    # can be changed dosage, stopped medication
    type = models.CharField(max_length=200, blank=True)
    reason_for_change = models.TextField(blank=True)
    date_changed = models.DateField(blank=True, null=True)



class PatientMedicationHistory(models.Model):
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE, related_name='patient_medication_history')
    type = models.CharField(max_length=100, blank=True)
    new_strength = models.CharField(max_length=100, blank=True)
    new_frequency = models.CharField(max_length=100, blank=True)
    prescription_type = models.CharField(max_length=100, blank=True)
    refills_given = models.SmallIntegerField(blank=True, null=True)


class PatientMedicationAuthorization(models.Model):
    #patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_medication_authorizations')
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE,
                                   related_name='medication_authorizations')
    authorized = models.BooleanField()
    authorization_number = models.CharField(max_length=500, blank=True)
    contact_method = models.TextField(blank=True)
    authorized_on = models.DateField(blank=True, null=True)
    date_of_next_authorization = models.DateField(blank=True, null=True)





class Guarantor(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_guarantors')
    guarantor_relationship_choices = [('self', 'Self'), ('parent', 'Parent'), ('spouse', 'Spouse')]
    relationship_to_patient = models.CharField(choices=guarantor_relationship_choices, max_length=20, blank=True,
                                               null=True)
    guarantor_first_name = models.CharField(max_length=30, blank=True)
    guarantor_last_name = models.CharField(max_length=30, blank=True)
    guarantor_middle_name = models.CharField(max_length=30, blank=True)


class PatientRequestUpdate(models.Model):
    request = models.ForeignKey('PatientRequest', on_delete=models.CASCADE, related_name='patient_request_updates')
    # patient_provided_update: models.BooleanField(default=False)
    update = models.TextField()

"""
patient request details object should look like this

{
    description:"",
    updates: []
    status: "",
    type: "",
}
"""


class PatientRequest(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_requests')
    request_types = [('medication', 'Medication Refill'),
                     ('insurance_authorization_medication', 'Medication Insurance Authorization'), ('other', 'Other'),
                     ('clinical_question', 'Clinical Question')]
    request_status_choices = [('active', 'Active'), ('inactive', 'Inactive'), ('complete', 'Complete'),
                              ('cancelled', 'Cancelled')]
    type = models.CharField(choices=request_types, max_length=50)
    details = JSONField(null=True)
    status = models.CharField(choices=request_status_choices, max_length=50)
    request_description = models.TextField()

"""
details object should look like this
{
    contact_numbers: [],
    demographics: {
        address: {
            street: '',
            street2: '',
            city: '',
            state: '',
            zip: ''
            }
    },
    allergies: [],
    history: {
        medical: [],
        surgical: [],
        family: [],
        social: [],
    } {
}
"""



class Patient(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=False)
    preferred_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    details = JSONField(null=True)
    ssn = models.IntegerField(blank=False)

    @property
    def display_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    type_choices = [('primary', 'primary'), ('secondary', 'secondary')]
    insurance_name = models.CharField(max_length=200, blank=True)
    tradingPartnerId = models.CharField(max_length=200, blank=True)
    primary = models.BooleanField(null=True, blank=True)
    group_ID = models.CharField(max_length=200, blank=True)
    bin_number = models.CharField(max_length=200, blank=True)
    pcn = models.CharField(max_length=200, blank=True)
    type = models.CharField(choices=type_choices, max_length=50, blank=True)
    member_id = models.CharField(max_length=30, blank=True)
    relationship_code = models.CharField(max_length=2, blank=True)
    # active = models.BooleanField(null=True)
    date_effective = models.DateField(blank=True, null=True)
    date_terminated = models.DateField(blank=True, null=True)
    copay_amount = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)

    @property
    def active(self):
        if self.date_terminated:
            return False
        else:
            return True







"""
class PatientRadiology(models.Model):
    test = models.CharField(max_length=200, blank=True)
    findings = models.TextField(blank=True)
    diagnosis = models.ManyToManyField(PatientDiagnosis, blank=True, related_name='radiology_history')

class ContactInformation(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_contact_methods')
    type = models.CharField(max_length=30, blank=True)
    number = PhoneNumberField(blank=True)
    #when_to_call = models.CharField(max_length=30, blank=True)
    special_instructions = models.TextField(blank=True)

class Allergy(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_allergies', blank=True, null=True)
    type = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    treatment = models.TextField(blank=True)

class SurgicalHistory(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_surgeries')
    procedure = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    additional_information = models.TextField(blank=True)
    performed_by = models.CharField(max_length=200, blank=True)
"""


"""
class PatientReports(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_reports')
    patient_report_type_choices = [('other_provider_notes', 'Clinical notes from other provider'),
                                   ('lab_reports', 'Lab Reports'), ('radiology_report', 'Radiology Report')]
    type = models.CharField(choices=patient_report_type_choices, max_length=30)
    file = models.FileField()
    received_on = models.DateField()
    provider_notes = models.TextField(blank=True)
"""


"""
class PatientDocumentation(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_documents')
    file = models.FileField()
    description = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
"""






"""
class Demographics(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='patient_demographics')
    race = models.CharField(max_length=50, default=not_listed)
    gender = models.CharField(max_length=50, default=not_listed)
    marital_status = models.CharField(max_length=50, default=not_listed)
    employment_status = models.CharField(max_length=50, default=not_listed)
    email = models.EmailField(max_length=50, blank=True)

class Address(models.Model):
    #patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_addresses')
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='patient_address')
    address_one = models.CharField(max_length=150, default=not_listed)
    address_two = models.CharField(max_length=50, default=not_listed)
    city = models.CharField(max_length=50, default=not_listed)
    state = models.CharField(max_length=50, default=not_listed)
    zip_code = models.CharField(max_length=50, default=not_listed)
"""


    # APPOINTMENTS (one to many)
    # Medications Field (one to many)
    # DIAGNOSIS FIELD (one to many)
    # Family Medical History field (one to many)
    # Medical History Field (one to many)
# I dont think we use this formfield anymore


