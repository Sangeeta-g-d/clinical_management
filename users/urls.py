from django.urls import path
from . import views

urlpatterns = [
    path('clinic_login',views.clinic_login, name="clinic_login"),
    path('clinic_register',views.clinic_register, name="clinic_register"),
]
