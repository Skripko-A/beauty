# Generated by Django 5.0.7 on 2024-08-01 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_alter_appointment_date_alter_appointment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 2, 7, 5, 43, 986536)),
        ),
    ]