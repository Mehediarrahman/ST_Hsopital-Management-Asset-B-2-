from django.contrib import admin
from .models import *


admin.site.register([UserModel, DepartmentModel, DoctorModel, PatientsModel])
# Register your models here.
