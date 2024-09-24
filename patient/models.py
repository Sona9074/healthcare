from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class PatientDetail(models.Model):
    GENDER_CHOICEs =(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
    )
    name = models.CharField(max_length = 200)
    age = models.CharField(max_length = 100)
    birthdate = models.DateField()
    phone = models.CharField(null=True,blank=True,max_length=10)
    gender = models.CharField(choices=GENDER_CHOICEs, max_length=10)
    address = models.TextField(null = True,blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated','created']

    def __str__(self):
        return str(self.name)
    
class MedicalRecord(models.Model):
    BLOODGROUP_CHOICEs =(
    ('A +ve','A +ve'),
    ('A -ve','A -ve'),
    ('B +ve','B +ve'),
    ('B -ve','B -ve'),
    ('AB +ve','AB +ve'),
    ('AB -ve','AB -ve'),
    ('O +ve','O +ve'),
    ('O -ve','O -ve')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.OneToOneField(PatientDetail,on_delete = models.CASCADE)
    height = models.CharField(null=True,blank=True,max_length=3)
    weight = models.CharField(null=True,blank=True,max_length=3)
    bloodgroup = models.CharField(null=True,blank=True,choices=BLOODGROUP_CHOICEs, max_length=100)
    medical_history = models.TextField(null=True,blank=True)
    prescription = models.TextField(null=True,blank=True)
    allergies = models.TextField(null=True,blank=True)
    last_checkup_date = models.DateField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.name)
    

class Appoinment(models.Model):
    MEDICAL_DEPARTMENT_CHOICEs =(
    ('Anesthetics','Anesthetics'),
    ('Cardiology','Cardiology'),
    ('Dermatology','Dermatology'),
    ('Ear, nose and throat (ENT)','Ear, nose and throat (ENT)'),
    ('Elderly services department','Elderly services department'),
    ('Gastroenterology','Gastroenterology'),
    ('General Surgery','General Surgery'),
    ('Hematology','Hematology'),
    ('Neurology','Neurology'),
    ('Nutrition and dietetics','Nutrition and dietetics'),
    ('Gynecology','Cardiology'),
    ('Oncology','Oncology'),
    ('Ophthalmology','Ophthalmology'),
    ('Orthopedics','Orthopedics'),
    ('Pediatrics','Pediatrics'),
    ('Physiotherapy','Physiotherapy')
    )
    appointment_no = models.CharField(null=True,blank=True,max_length=10)
    date = models.DateTimeField()
    name = models.ForeignKey(PatientDetail,on_delete=models.CASCADE)
    doctor_name = models.CharField(null=True,blank=True,max_length=20)
    medical_department = models.CharField(null=True,blank=True,choices=MEDICAL_DEPARTMENT_CHOICEs, max_length=100)
    notes = models.TextField(null = True,blank = True)
    updated = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return str(self.name)


    