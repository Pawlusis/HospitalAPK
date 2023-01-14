from django.db import models

# Create your models here.

class Patients(models.Model):
    firstname_patient = models.CharField(max_length=64)
    lastname_patient = models.CharField(max_length=64)
    birthdate_patient = models.DateField()
    admittingtime_patient = models.DateTimeField()
    dischargetime_patient = models.DateTimeField(default='',blank=True,null=True)

    def __str__(self):
        return self.firstname_patient + ' ' + self.lastname_patient

