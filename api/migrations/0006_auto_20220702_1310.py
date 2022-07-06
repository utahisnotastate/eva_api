# Generated by Django 3.0.6 on 2022-07-02 13:10

import api.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220702_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=api.models.default_patient_details),
        ),
    ]
