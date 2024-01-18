# Generated by Django 5.0.1 on 2024-01-16 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_appoinments_medicalrecord_patientdetails_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('address', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='bloodgroup',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.RenameModel(
            old_name='Appoinments',
            new_name='Appoinment',
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientdetail'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patientdetail'),
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
    ]
