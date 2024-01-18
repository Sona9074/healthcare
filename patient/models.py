from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class PatientDetail(models.Model):
    GENDER_CHOICEs =(
    ('Male','Male'),
    ('Female','Female')
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
        ordering = ['-updated','-created']

    def __str__(self):
        return str(self.name)
    
class MedicalRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.OneToOneField(PatientDetail,on_delete = models.CASCADE)
    bloodgroup = models.CharField(max_length = 10, null=True,blank=True)
    prescription = models.TextField(null=True,blank=True)
    allergies = models.TextField(null=True,blank=True)
    last_checkup_date = models.DateField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.name)
    

class Appoinment(models.Model):
    name = models.ForeignKey(PatientDetail,on_delete=models.CASCADE)
    date = models.DateTimeField()
    purpose = models.CharField(max_length = 200)
    notes = models.TextField(null = True,blank = True)
   
    def __str__(self):
        return str(self.name)


    