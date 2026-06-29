from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    def __str__(self):
        return self.username


class DepartmentModel(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
    
class DoctorModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    specialization = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    dept = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class PatientsModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    age = models.IntegerField(null=True)
    disease = models.CharField(max_length=250, null=True)
    admitted_date = models.DateField(auto_now=False, auto_now_add=True)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name