# Generated by Django 5.0.6 on 2024-06-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_newuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='available_timings',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='newuser',
            name='qualification',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='newuser',
            name='specialization',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
