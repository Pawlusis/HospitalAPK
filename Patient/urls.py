from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients_list/', patients_list),
    path('new/', new_patient),
]