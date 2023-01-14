from django.contrib import admin
from .models import *

# # Register your models here.
# admin.site.register(Patients)
# admin.site.register(HospitalBed)
# admin.site.register(HospitalRoom)
# admin.site.register(HospitalWard)

@admin.register(Patients)
class PacjentAdmin(admin.ModelAdmin):
    # fields = ["firstname_patient"]
    list_display = ["lastname_patient", "firstname_patient" ]
    search_fields = ["firstname_patient", "lastname_patient"]
