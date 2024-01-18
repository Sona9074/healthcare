from django.shortcuts import render,redirect
from .models import PatientDetail,MedicalRecord,Appoinment
from .forms import RecordForm,MedicalRecordForm,AppoinmentForm


# Create your views here.

# records =[
#     {'id':1,'name':'Personal information'},
#     {'id':2,'name':'Medical history'},
#     {'id':3,'name':'Appoinments'},
# ]

def home(request):
    records = PatientDetail.objects.all()
    context = {'records':records}
    return render(request,'patient/home.html',context)

def record(request,pk):
    record = PatientDetail.objects.get(id=pk)
    context = {'record':record}
    return render(request,'patient/record.html',context)

def createRecord(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={'form':form}
    return render(request,'patient/patient_form.html',context)

def updateRecord(request,pk):
    record = PatientDetail.objects.get(id=pk)
    form = RecordForm(instance=record)

    if request.method == 'POST':
        form = RecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'patient/patient_form.html',context)

def deleteRecord(request,pk):
    record = PatientDetail.objects.get(id=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('home')
    return render(request,'patient/delete.html',{'obj':record})


def medicalHistory(request):
    form = MedicalRecordForm()
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={'form':form}
    return render(request,'patient/patient_form.html',context)

def appoinments(request):
    form = AppoinmentForm()
    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={'form':form}
    return render(request,'patient/patient_form.html',context)


def medical(request):
    medical = MedicalRecord.objects.all()
    context = {'medical':medical}
    return render(request,'patient/medical_history.html',context)

def appoinment(request):
    appoinment = Appoinment.objects.all()
    context = {'appoinment':appoinment}
    return render(request,'patient/appoinment.html',context)


