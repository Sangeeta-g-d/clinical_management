from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 
from django.utils import timezone

class NewUser(AbstractUser):
    user_type = models.CharField(max_length=100, default='patient')
    phone_no = models.CharField(max_length=100, default='employee')
    address = models.CharField(max_length=100, default='employee')
    city = models.CharField(max_length=100, default='employee')
    qualification=models.CharField(max_length=100, default=' ')
    specialization=models.CharField(max_length=100, default=' ')
    available_timings=models.CharField(max_length=100, default=' ')
    added_by=models.CharField(max_length=100, default=' ')


class Appointments(models.Model):
    clinic_id = models.CharField(max_length=100, default='patient')
    patient_id = models.ForeignKey('NewUser', on_delete=models.CASCADE, related_name='patient_appointments')
    doctor_id = models.ForeignKey('NewUser', on_delete=models.CASCADE, related_name='doctor_appointments')
    timings = models.DateTimeField(default=timezone.now)
