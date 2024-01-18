from django.contrib import admin

# Register your models here.

from .models import PatientDetail,MedicalRecord,Appoinment

admin.site.register(PatientDetail)
admin.site.register(MedicalRecord)
admin.site.register(Appoinment)