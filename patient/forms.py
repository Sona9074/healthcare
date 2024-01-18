from django.forms import ModelForm
from .models import PatientDetail,MedicalRecord,Appoinment

class RecordForm(ModelForm):
    class Meta:
        model = PatientDetail
        fields = '__all__'

class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class AppoinmentForm(ModelForm):
    class Meta:
        model = Appoinment
        fields = '__all__'