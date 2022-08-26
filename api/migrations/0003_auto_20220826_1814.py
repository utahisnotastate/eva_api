# Generated by Django 3.0.6 on 2022-08-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220803_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, default='scheduled', max_length=100, null=True),
        ),
    ]
