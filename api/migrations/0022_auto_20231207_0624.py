# Generated by Django 3.0.6 on 2023-12-07 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_appointment_ainote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='ainote',
            new_name='note',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providers', to='api.Provider'),
        ),
    ]
