# Generated by Django 3.0.6 on 2022-08-26 23:11

import api.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220826_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=api.models.default_form_details, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=api.models.default_request_details),
        ),
    ]