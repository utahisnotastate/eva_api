# Generated by Django 3.0.6 on 2023-03-21 03:27

import api.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20230316_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=api.models.default_patient_details),
        ),
    ]