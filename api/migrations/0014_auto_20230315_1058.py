# Generated by Django 3.0.6 on 2023-03-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20230315_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
