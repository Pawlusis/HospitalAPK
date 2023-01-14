from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Patients
from .forms import PatientForm


# Create your views here.

def patients_list(request):
    # return HttpResponse("<h1>Działa</h2>")
    allpatients = Patients.objects.all()
    return render(request,'patients.html', {'patients': allpatients})

class new_patient(PatientForm):
    form_class = PatientForm
    template_name = 'new_patient.html'  # Replace with your template.
    success_url = 'patients.html'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('attachments')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# def new_patient(request):
#     form = PatientForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#
#     return render(request, 'new_patient.html', {'form':form})
