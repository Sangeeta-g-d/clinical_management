from django.urls import path
from . import views

urlpatterns = [
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_db',views.admin_db,name="admin_db"),
    path('approve_clinic/<int:id>',views.approve_clinic,name="approve_clinic"),
    path('delete_clinic/<int:id>',views.delete_clinic,name="delete_clinic"),
    path('clinic_login',views.clinic_login, name="clinic_login"),
    path('clinic_register',views.clinic_register, name="clinic_register"),
    path('clinic_db',views.clinic_db, name="clinic_db"),
    path('add_doctor',views.add_doctor, name="add_doctor"),
]
