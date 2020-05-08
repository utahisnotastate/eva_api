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


class PracticeUpdate(models.Model):
    update = models.TextField()
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


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
    type_choices = [('first_appointment', 'First Appointment'), ('medication_management', 'Medication Management'),
                    ('follow_up', 'Follow Up'), ('appointment', 'Appointment')]
    type = models.CharField(choices=type_choices, max_length=100, default=type_choices[3][1])
    status_choices = [('scheduled', 'Scheduled'), ('arrived', 'Arrived'), ('in_exam_room', 'In Exam Room'),
                      ('in_progress', 'In progress'), ('complete', 'Complete'), ('cancelled', 'Cancelled')]
    status = models.CharField(choices=status_choices, max_length=100, default=status_choices[0][1])
    start = models.DateTimeField()
    # rescheduledfrom = models.IntegerField(default=0)
    end = models.DateTimeField()
    scheduled_on = models.DateTimeField(auto_now_add=True)


# class AppointmentAssessment(models.Model):
# appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='assessments')
#  icd_code = models.CharField(max_length=10, blank=True, null=True)
# icd_description = models.CharField(max_length=100, blank=True, null=True)


class AppointmentFinding(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_findings')
    form_field = models.ForeignKey('FormField', on_delete=models.CASCADE, related_name='appointment_findings_fields')
    value = models.TextField()


class Vital(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='vitals')
    systolic_pressure = models.PositiveIntegerField(blank=True, null=True)
    diastolic_pressure = models.PositiveIntegerField(blank=True, null=True)
    temperature_value = models.PositiveIntegerField(blank=True, null=True)
    temperature_unit_choices = [('fahrenheit', 'Fahrenheit'), ('celsius', 'Celsius')]
    temperature_unit = models.CharField(choices=temperature_unit_choices, max_length=30, blank=True, null=True)
    pulse = models.PositiveIntegerField(blank=True, null=True)
    weight_value = models.PositiveIntegerField(blank=True, null=True)
    weight_unit_choices = [('pounds', 'Pounds'), ('kilograms', 'Kilograms')]
    weight_unit = models.CharField(choices=weight_unit_choices, max_length=30, blank=True, null=True)


class FormFieldOption(models.Model):
    form_field = models.ForeignKey('FormField', on_delete=models.CASCADE, related_name='field_options')
    label = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)


class FormField(models.Model):
    form = models.ForeignKey('Form', on_delete=models.CASCADE, related_name='form_fields')
    position = models.SmallIntegerField(null=True, blank=True)
    has_options = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class Form(models.Model):
    form_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=False)


class ComplaintTherapeuticAttempt(models.Model):
    complaint = models.ForeignKey('Complaint', on_delete=models.CASCADE, related_name='complaint_therapeutic_attempts')
    type = models.CharField(max_length=100)
    description = models.TextField()
    helped_choices = (
        (None, 'Unchecked'),
        (True, 'Helped'),
        (False, 'Didnt Help')
    )
    helped = models.NullBooleanField(choices=helped_choices, default=None)


class Complaint(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='complaints')
    # icd_code = models.CharField(max_length=10, blank=True, null=True)
    # icd_description = models.CharField(max_length=100, blank=True, null=True)
    complaint_name = models.CharField(max_length=100, blank=True, null=True)
    complaint_description = models.TextField(blank=True, null=True)
    onset_number = models.SmallIntegerField()
    onset_unit_choices = [('day', 'Day(s)'), ('weeks', 'Week(s)'), ('months', 'Month(s)'), ('years', 'Years')]
    onset_unit = models.CharField(choices=onset_unit_choices, max_length=40, blank=True, null=True)
    onset_doesnt_remember = models.BooleanField(default=False)
    onset_not_asked = models.BooleanField(default=True)
    location_choices = [('head', 'Head'), ('neck', 'Neck'), ('upper_extremity', 'Upper Extremity'), ('chest', 'Chest'),
                        ('abdomen', 'abdomen'), ('groin', 'Groin'), ('lower_extremity', 'Lower Extremity')]
    location = models.CharField(choices=location_choices, max_length=30, blank=True, null=True)
    patient_belief_caused_by = models.TextField(blank=True, null=True)
    patient_therapeutic_attempts = models.TextField(blank=True, null=True)
    patients_guess = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)


class AssessmentRelatedTo(models.Model):
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='assessment_related_to')
    category_choices = [('complaint', 'Complaint'), ('review_of_systems', 'Review of Systems Finding'),
                        ('physical_exam', 'Physical Exam Finding')]
    category = models.CharField(choices=category_choices, blank=True, null=True, max_length=50)


class Assessment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='assessments')
    icd_code = models.CharField(max_length=10, blank=True, null=True)
    icd_description = models.CharField(max_length=100, blank=True, null=True)
    other_assessment = models.TextField(blank=True, null=True)


class AppointmentPlan(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_plans')
    plan_choices = [('no_follow_up_necessary', 'No follow up necessary'),
                    ('prescribe_medication', 'Prescribe Medication'), ('order_labs', 'Order Labs'),
                    ('order_imaging', 'Order Imaging'), ('specialist_referral', 'Specialist Referral'),
                    ('schedule_follow_up', 'Schedule Follow Up')]
    plan = models.CharField(choices=plan_choices, default='no_follow_up_necessary', max_length=60)
    plan_details = models.TextField(blank=True, null=True)


class Summary(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='summary')
    summary = models.TextField(blank=True, null=True)


# Patient Models


class SurgicalHistory(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_surgeries')
    procedure = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    additional_information = models.TextField(null=True, blank=True);
    performed_by = models.CharField(max_length=200, blank=True, null=True)


class PatientReports(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_reports')
    patient_report_type_choices = [('other_provider_notes', 'Clinical notes from other provider'),
                                   ('lab_reports', 'Lab Reports'), ('radiology_report', 'Radiology Report')]
    type = models.CharField(choices=patient_report_type_choices, max_length=30)
    file = models.FileField()
    received_on = models.DateField()
    provider_notes = models.TextField(blank=True, null=True)


class PatientDocumentation(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_documents')
    file = models.FileField()
    description = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)


class PatientDiagnosis(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_diagnoses')
    diagnosis_icd_code = models.CharField(max_length=200, blank=True, null=True)
    diagnosis_description = models.CharField(max_length=200, blank=True, null=True)
    diagnosis_status_choices = [('active', 'Active'), ('inactive', 'Inactive')]
    diagnosis_status = models.CharField(choices=diagnosis_status_choices, max_length=20, blank=True, null=True)
    diagnosed_on = models.DateField(blank=True, null=True)
    diagnosed_by = models.CharField(max_length=200, blank=True, null=True)


class PatientMedication(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_medications')
    diagnosis = models.ForeignKey(PatientDiagnosis, on_delete=models.CASCADE,
                                  related_name='patient_medications_for_diagnosis', blank=True, null=True)
    prescribed_by = models.CharField(max_length=300)
    last_written_on = models.DateField(blank=True, null=True)
    refills_given = models.SmallIntegerField(default=0)
    requires_authorization = models.BooleanField(null=True)
    name = models.CharField(max_length=200)
    dosage = models.PositiveSmallIntegerField()
    dosage_unit = models.CharField(max_length=100)
    frequency = models.CharField(max_length=400)
    date_started = models.DateField(blank=True, null=True)
    date_stopped = models.DateField(blank=True, null=True)
    stoppage_reason = models.TextField(blank=True, null=True)
    # diagnosis = models.TextField()


class PatientMedicationAuthorization(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_medication_authorizations')
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE,
                                   related_name='medication_authorizations')
    authorized = models.BooleanField()
    authorization_number = models.CharField(max_length=500)
    contact_method = models.TextField()
    authorized_on = models.DateField()
    date_of_next_authorization = models.DateField(blank=True, null=True)


class ContactInformation(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_contact_methods')
    contact_types = [('cell', 'Cell'), ('home', 'Home'), ('work', 'Work')]
    when_to_call_choices = [('morning', 'Morning'), ('daytime', 'Daytime'), ('evening', 'Evening'),
                            ('anytime', 'Anytime')]
    type = models.CharField(choices=contact_types, max_length=5)
    number = PhoneNumberField()
    when_to_call = models.CharField(choices=when_to_call_choices, max_length=20)
    special_instructions = models.TextField(blank=True, null=True)


class Guarantor(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_guarantors')
    guarantor_relationship_choices = [('self', 'Self'), ('parent', 'Parent'), ('spouse', 'Spouse')]
    relationship_to_patient = models.CharField(choices=guarantor_relationship_choices, max_length=20, blank=True,
                                               null=True)
    guarantor_first_name = models.CharField(max_length=30, blank=True, null=True)
    guarantor_last_name = models.CharField(max_length=30, blank=True, null=True)
    guarantor_middle_name = models.CharField(max_length=30, blank=True, null=True)


class PatientRequestUpdate(models.Model):
    request = models.ForeignKey('PatientRequest', on_delete=models.CASCADE, related_name='patient_request_updates')
    # patient_provided_update: models.BooleanField(default=False)
    update = models.TextField()


class PatientRequest(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    request_types = [('medication', 'Medication Refill'),
                     ('insurance_authorization_medication', 'Medication Insurance Authorization'), ('other', 'Other'),
                     ('clinical_question', 'Clinical Question')]
    request_status_choices = [('active', 'Active'), ('inactive', 'Inactive'), ('complete', 'Complete'),
                              ('cancelled', 'Cancelled')]
    type = models.CharField(choices=request_types, max_length=50)
    status = models.CharField(choices=request_status_choices, max_length=50)
    request_description = models.TextField()


class Address(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_addresses')
    active = models.BooleanField()
    address_one = models.CharField(max_length=50, blank=True, null=True)
    address_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)


class Insurance(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insurances')
    type_choices = [('primary', 'primary'), ('secondary', 'secondary')]
    insurance_name = models.CharField(max_length=200, blank=True, null=True)
    tradingPartnerId = models.CharField(max_length=200, blank=True, null=True)
    group_ID = models.CharField(max_length=200, blank=True, null=True)
    bin_number = models.CharField(max_length=200, blank=True, null=True)
    pcn = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(choices=type_choices, max_length=50, blank=True, null=True)
    member_id = models.CharField(max_length=30, blank=True, null=True)
    relationship_code = models.CharField(max_length=2, blank=True, null=True)
    active = models.BooleanField(null=True)
    date_effective = models.DateField(blank=True, null=True)
    date_terminated = models.DateField(blank=True, null=True)
    copay_amount = models.DecimalField(decimal_places=2, max_digits=8)


class Demographics(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_demographics')
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ]
    RACE_CHOICES = [('black-non-hispanic', 'Black - Non Hispanic'), ('caucasian', 'Caucasian'), ('other', 'Other')]
    MARITAL_CHOICES = [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widow', 'Widow')]
    EMPLOYMENT_CHOICES = [('full_time', 'Employed Full Time'), ('part_time', 'Employed Part Time'),
                          ('unemployed', 'Unemployed')]
    race = models.CharField(choices=RACE_CHOICES, max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    marital_status = models.CharField(choices=MARITAL_CHOICES, max_length=20)
    employment_status = models.CharField(choices=EMPLOYMENT_CHOICES, max_length=20)
    email = models.EmailField()


# Patient Allergy Models


class LatexAllergy(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    STATUS_CHOICES = [('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('present', 'Present')]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, null=True)


class PollenAllergy(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    STATUS_CHOICES = [('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('present', 'Present')]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, null=True)


class PetAllergies(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    STATUS_CHOICES = [('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('dogs', 'Dogs'), ('cats', 'Cats'),
                      ('both', 'Both')]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, null=True)


class DrugAllergies(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_drug_allergies')
    drug = models.CharField(max_length=200, blank=True, null=True)


class FoodAllergies(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_food_allergies')
    food = models.CharField(max_length=200, blank=True, null=True)


class InsectAllergies(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='patient_insect_allergies')
    insect = models.CharField(max_length=200, blank=True, null=True)


class Patient(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=False)
    preferred_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=False)
    ssn = models.BigIntegerField(blank=False)

    @property
    def display_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    # APPOINTMENTS (one to many)
    # Medications Field (one to many)
    # DIAGNOSIS FIELD (one to many)
    # Family Medical History field (one to many)
    # Medical History Field (one to many)
