# Generated by Django 3.0.6 on 2020-07-03 00:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('first_appointment', 'First Appointment'), ('medication_management', 'Medication Management'), ('follow_up', 'Follow Up'), ('appointment', 'Appointment')], default='Appointment', max_length=100)),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('arrived', 'Arrived'), ('in_exam_room', 'In Exam Room'), ('in_progress', 'In progress'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], default='Scheduled', max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('scheduled_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icd_code', models.CharField(blank=True, max_length=10, null=True)),
                ('icd_description', models.CharField(blank=True, max_length=100, null=True)),
                ('other_assessment', models.TextField(blank=True, null=True)),
                ('based_on', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_name', models.CharField(blank=True, max_length=100, null=True)),
                ('complaint_description', models.TextField(blank=True, null=True)),
                ('onset_number', models.SmallIntegerField()),
                ('onset_unit', models.CharField(blank=True, choices=[('day', 'Day(s)'), ('weeks', 'Week(s)'), ('months', 'Month(s)'), ('years', 'Years')], max_length=40, null=True)),
                ('onset_doesnt_remember', models.BooleanField(default=False)),
                ('onset_not_asked', models.BooleanField(default=True)),
                ('location', models.CharField(blank=True, choices=[('head', 'Head'), ('neck', 'Neck'), ('upper_extremity', 'Upper Extremity'), ('chest', 'Chest'), ('abdomen', 'abdomen'), ('groin', 'Groin'), ('lower_extremity', 'Lower Extremity')], max_length=30, null=True)),
                ('patient_belief_caused_by', models.TextField(blank=True, null=True)),
                ('patient_therapeutic_attempts', models.TextField(blank=True, null=True)),
                ('patients_guess', models.TextField(blank=True, null=True)),
                ('other_notes', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('form', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(blank=True, null=True)),
                ('has_options', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False)),
                ('label', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='api.Form')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('preferred_name', models.CharField(blank=True, max_length=30)),
                ('date_of_birth', models.DateField()),
                ('ssn', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_icd_code', models.CharField(blank=True, max_length=200, null=True)),
                ('diagnosis_description', models.CharField(blank=True, max_length=200, null=True)),
                ('diagnosis_status', models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=20, null=True)),
                ('diagnosed_on', models.DateField(blank=True, null=True)),
                ('diagnosed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_diagnoses', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribed_by', models.CharField(max_length=300)),
                ('last_written_on', models.DateField(blank=True, null=True)),
                ('refills_given', models.SmallIntegerField(default=0)),
                ('requires_authorization', models.BooleanField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('dosage', models.PositiveSmallIntegerField()),
                ('dosage_unit', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=400)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_stopped', models.DateField(blank=True, null=True)),
                ('stoppage_reason', models.TextField(blank=True, null=True)),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_medications_for_diagnosis', to='api.PatientDiagnosis')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_medications', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('medication', 'Medication Refill'), ('insurance_authorization_medication', 'Medication Insurance Authorization'), ('other', 'Other'), ('clinical_question', 'Clinical Question')], max_length=50)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], max_length=50)),
                ('request_description', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address_one', models.CharField(max_length=500)),
                ('address_two', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=12)),
                ('npi', models.CharField(max_length=100)),
                ('first_appointment_starts', models.TimeField()),
                ('last_appointment_ends', models.TimeField()),
                ('close', models.TimeField()),
                ('tax_id', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.TextField()),
                ('display', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Dr', 'Dr'), ('Nurse', 'Nurse')], max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('npi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic_pressure', models.PositiveIntegerField(blank=True, null=True)),
                ('diastolic_pressure', models.PositiveIntegerField(blank=True, null=True)),
                ('temperature_value', models.PositiveIntegerField(blank=True, null=True)),
                ('temperature_unit', models.CharField(blank=True, choices=[('fahrenheit', 'Fahrenheit'), ('celsius', 'Celsius')], max_length=30, null=True)),
                ('pulse', models.PositiveIntegerField(blank=True, null=True)),
                ('weight_value', models.PositiveIntegerField(blank=True, null=True)),
                ('weight_unit', models.CharField(blank=True, choices=[('pounds', 'Pounds'), ('kilograms', 'Kilograms')], max_length=30, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vitals', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('performed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_surgeries', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='PollenAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('present', 'Present')], max_length=50, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PetAllergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('dogs', 'Dogs'), ('cats', 'Cats'), ('both', 'Both')], max_length=50, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRequestUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.TextField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_request_updates', to='api.PatientRequest')),
            ],
        ),
        migrations.CreateModel(
            name='PatientReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('other_provider_notes', 'Clinical notes from other provider'), ('lab_reports', 'Lab Reports'), ('radiology_report', 'Radiology Report')], max_length=30)),
                ('file', models.FileField(upload_to='')),
                ('received_on', models.DateField()),
                ('provider_notes', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_reports', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicationAuthorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized', models.BooleanField()),
                ('authorization_number', models.CharField(max_length=500)),
                ('contact_method', models.TextField()),
                ('authorized_on', models.DateField()),
                ('date_of_next_authorization', models.DateField(blank=True, null=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_authorizations', to='api.PatientMedication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_medication_authorizations', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDocumentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_documents', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='LatexAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('unchecked', 'Unchecked'), ('not_present', 'Not Present'), ('present', 'Present')], max_length=50, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(blank=True, max_length=200, null=True)),
                ('tradingPartnerId', models.CharField(blank=True, max_length=200, null=True)),
                ('group_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('bin_number', models.CharField(blank=True, max_length=200, null=True)),
                ('pcn', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=50, null=True)),
                ('member_id', models.CharField(blank=True, max_length=30, null=True)),
                ('relationship_code', models.CharField(blank=True, max_length=2, null=True)),
                ('active', models.BooleanField(null=True)),
                ('date_effective', models.DateField(blank=True, null=True)),
                ('date_terminated', models.DateField(blank=True, null=True)),
                ('copay_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_insurances', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='InsectAllergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insect', models.CharField(blank=True, max_length=200, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_insect_allergies', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_to_patient', models.CharField(blank=True, choices=[('self', 'Self'), ('parent', 'Parent'), ('spouse', 'Spouse')], max_length=20, null=True)),
                ('guarantor_first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('guarantor_last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('guarantor_middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_guarantors', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='FormFieldOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('form_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_options', to='api.FormField')),
            ],
        ),
        migrations.CreateModel(
            name='FoodAllergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(blank=True, max_length=200, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_food_allergies', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='DrugAllergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(blank=True, max_length=200, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_drug_allergies', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('black-non-hispanic', 'Black - Non Hispanic'), ('caucasian', 'Caucasian'), ('other', 'Other')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widow', 'Widow')], max_length=20)),
                ('employment_status', models.CharField(choices=[('full_time', 'Employed Full Time'), ('part_time', 'Employed Part Time'), ('unemployed', 'Unemployed')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_demographics', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cell', 'Cell'), ('home', 'Home'), ('work', 'Work')], max_length=5)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('when_to_call', models.CharField(choices=[('morning', 'Morning'), ('daytime', 'Daytime'), ('evening', 'Evening'), ('anytime', 'Anytime')], max_length=20)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_contact_methods', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintTherapeuticAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('helped', models.NullBooleanField(choices=[(None, 'Unchecked'), (True, 'Helped'), (False, 'Didnt Help')], default=None)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint_therapeutic_attempts', to='api.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='api.Appointment')),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Guarantor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='api.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentRelatedTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('complaint', 'Complaint'), ('review_of_systems', 'Review of Systems Finding'), ('physical_exam', 'Physical Exam Finding')], max_length=50, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_related_to', to='api.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('no_follow_up_necessary', 'No follow up necessary'), ('prescribe_medication', 'Prescribe Medication'), ('order_labs', 'Order Labs'), ('order_imaging', 'Order Imaging'), ('specialist_referral', 'Specialist Referral'), ('schedule_follow_up', 'Schedule Follow Up')], default='no_follow_up_necessary', max_length=60)),
                ('plan_details', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_plans', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('form_type', models.CharField(max_length=100)),
                ('form', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_forms', to='api.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentFinding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('findings', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_findings', to='api.Appointment')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_form_findings', to='api.Form')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.Provider'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('address_one', models.CharField(blank=True, max_length=50, null=True)),
                ('address_two', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_addresses', to='api.Patient')),
            ],
        ),
    ]
