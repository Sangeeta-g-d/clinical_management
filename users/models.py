from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 

class NewUser(AbstractUser):
    user_type = models.CharField(max_length=100, default='patient')
    phone_no = models.CharField(max_length=100, default='employee')
    address = models.CharField(max_length=100, default='employee')
    city = models.CharField(max_length=100, default='employee')