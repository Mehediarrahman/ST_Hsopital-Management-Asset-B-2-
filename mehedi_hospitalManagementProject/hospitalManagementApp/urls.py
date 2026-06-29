from django.urls import path
from .views import *

urlpatterns = [
    path('', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('dashboard/', dashboardPage, name='dashboard'),
    path('addDepartment/', addDepartmentPage, name='addDepartment'),
    path('addDoctor/', addDoctorPage, name='addDoctor'),
    path('addPatient/', addpatientPage, name='addPatient'),
    path('edit_Dept/<int:id>/', edit_Deptpage, name='edit_Dept'),
    
    path('editDoctor/<int:id>/', editDoctorPage, name='editDoctor'),
    path('deleteDoctor/<int:id>/', deleteDoctorPage, name='deleteDoctor'),
]
