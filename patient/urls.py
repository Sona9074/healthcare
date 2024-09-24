from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('record/<str:pk>/',views.record,name="record"),
    path('create-record/',views.createRecord,name="create-record"),
    path('update-record/<str:pk>/',views.updateRecord,name="update-record"),
    path('delete-record/<str:pk>/',views.deleteRecord,name="delete-record"),
    path('medical-history/',views.medicalHistory,name="medical-history"),
    path('appoinments/',views.appoinments,name="appoinments"),
    path('medical/<str:pk>/',views.medical,name="medical"),
    path('appoinment/<str:pk>/',views.appoinment,name="appoinment"),
    path('update-medical-history/<str:pk>/',views.updateMedicalHistory,name="update-medical-history"),
    path('update-appointment/<str:pk>/',views.updateAppointment,name="update-appointment"),
    path('delete-medical-record/<str:pk>/',views.deleteMedicalRecord,name="delete-medical-record"),
    path('delete-appointment/<str:pk>/',views.deleteAppointment,name="delete-appointment"),
]