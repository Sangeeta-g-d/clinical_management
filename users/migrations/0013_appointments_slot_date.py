# Generated by Django 5.0.6 on 2024-06-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_appointments_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='slot_date',
            field=models.CharField(default='', max_length=400),
        ),
    ]
