from django.urls import path
from . import views

urlpatterns = [
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_db',views.admin_db,name="admin_db"),
    path('doctor_login',views.doctor_login,name="doctor_login"),
    path('doctor_db',views.doctor_db,name="doctor_db"),
    path('approve_clinic/<int:id>',views.approve_clinic,name="approve_clinic"),
    path('delete_clinic/<int:id>',views.delete_clinic,name="delete_clinic"),
    path('clinic_login',views.clinic_login, name="clinic_login"),
    path('clinic_register',views.clinic_register, name="clinic_register"),
    path('admin_logout',views.admin_logout, name="admin_logout"),
    path('clinic_db',views.clinic_db, name="clinic_db"),
    path('add_doctor',views.add_doctor, name="add_doctor"),
    path('edit_doc_info/<int:id>',views.edit_doc_info, name="edit_doc_info"),
    path('patient_login',views.patient_login, name="patient_login"),
    path('patient_register',views.patient_register, name="patient_register"),
    path('patient_db',views.patient_db, name="patient_db"),
    path('book_appointment',views.book_appointment, name="book_appointment"),
    path('doctor_appo/<int:id>',views.doctor_appo, name="doctor_appo"),
    path('patient_logout',views.patient_logout, name="patient_logout"),
    path('clinic_logout',views.clinic_logout, name="clinic_logout"),
    path('appointment_list',views.appointment_list, name="appointment_list"),
    path('doctor_login',views.doctor_login, name="doctor_login"),
    path('doctor_db',views.doctor_db, name="doctor_db"),
   
    path('set_timing/<int:app_id>',views.set_timing, name="set_timing"),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('doctor_prescription', views.doctor_prescription, name='doctor_prescription'),
]
