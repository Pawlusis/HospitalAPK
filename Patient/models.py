from django.db import models

# Create your models here.

class Patients(models.Model):
    firstname_patient = models.CharField(max_length=64)
    lastname_patient = models.CharField(max_length=64)
    birthdate_patient = models.DateField()
    admittingtime_patient = models.DateTimeField()
    dischargetime_patient = models.DateTimeField(default='', blank=True, null=True)
    decribe_patient = models.TextField()


    def __str__(self):
        return self.firstname_patient + ' ' + self.lastname_patient

class HospitalBed(models.Model):
    number_of_bed = models.IntegerField()
    type_of_bed = models.CharField(max_length=20)


class HospitalRoom(models.Model):
    number_of_room = models.IntegerField()
    type_of_room = models.CharField(max_length=20)
    count_of_beds = models.IntegerField()

    def __str__(self):
        return self.number_of_room


class HospitalWard(models.Model):
    name_of_ward = models.CharField(max_length=64)
    count_of_rooms = models.IntegerField()

    def __str__(self):
        return self.name_of_ward


