# Generated by Django 3.0.6 on 2023-03-08 18:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20230301_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]