from django.urls import path
from . import views

urlpatterns = [
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_db',views.admin_db,name="admin_db"),
    path('approve_clinic/<int:id>',views.approve_clinic,name="approve_clinic"),
    path('delete_clinic/<int:id>',views.delete_clinic,name="delete_clinic"),
]