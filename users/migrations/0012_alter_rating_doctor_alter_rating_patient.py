# Generated by Django 5.0.6 on 2024-06-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='doctor',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='rating',
            name='patient',
            field=models.CharField(default='', max_length=300),
        ),
    ]
