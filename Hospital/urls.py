from django.urls import path, include
from Patient.views import *

urlpatterns = [
    path('patients/', include("Patient.urls"))
]
