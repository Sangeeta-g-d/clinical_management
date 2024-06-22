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
    patient_id = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor_id = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='doctor_appointments')
    timings = models.DateTimeField(default=timezone.now)
    slot = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient_id} with {self.doctor_id} on {self.timings}"

class AppointmentTimings(models.Model):
    appo_id = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    date = models.DateField()
    slot_timing = models.CharField(max_length=300, default='')

    def __str__(self):
        return f"{self.appo_id} - {self.date} - {self.slot_timing}"
    

class Rating(models.Model):
    patient =  models.CharField(max_length=300, default='')
    doctor = models.CharField(max_length=300, default='')
    rating = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):
    appo_id = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=600, default='')
    date = models.DateTimeField(default=timezone.now, editable=False)  # Automatically sets the current date and time when created

    def __str__(self):
        return f"Prescription for {self.appo_id.patient_id.first_name} on {self.date}"
    
