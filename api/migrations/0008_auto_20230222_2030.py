# Generated by Django 3.0.6 on 2023-02-22 20:30

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230222_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='type',
        ),
        migrations.AddField(
            model_name='appointment',
            name='fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict), blank=True, default=list, size=None),
        ),
    ]