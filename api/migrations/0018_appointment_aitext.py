# Generated by Django 3.0.6 on 2023-09-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20230323_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='aitext',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]