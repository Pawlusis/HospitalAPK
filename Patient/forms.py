from django.forms import ModelForm
from django import forms
from .models import Patients

class PatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["firstname_patient", "lastname_patient", "birthdate_patient", "admittingtime_patient", "dischargetime_patient", "decribe_patient"]
        attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))