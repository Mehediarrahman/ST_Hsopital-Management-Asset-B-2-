from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout
def registerPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_exist = UserModel.objects.filter(username=username).exists()
        email_exist = UserModel.objects.filter(email=email).exists()

        if user_exist or email_exist:
            messages.error(request, "User or email Already Exist")
        else:
            if password == confirm_password:
                if len(password) > 8:

                    user = UserModel.objects.create_user(
                        username= username,
                        email=email,
                        password=password
                    )
                    messages.success(request, "User Created Successfully")
                    if user:
                        login(request, user)
                        return redirect('dashboard')
                else:
                    messages.warning(request, "Password Should Be More Than 8 Char")
    return render(request, 'auth/register.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, 'User Logged In Successfully')
            return redirect('dashboard')
    return render(request, 'auth/login.html')

def logoutPage(req):
    logout(req)
    messages.warning(req, "User Logged Out Finally")
    return redirect('login')

def dashboardPage(request):
    return render(request, 'pages/dashboard.html')

def addDepartmentPage(request):
    if request.method == "POST":
        name = request.POST.get("dept_name")

        DepartmentModel.objects.create(
            name = name
        )

        messages.success(request, "Department Successfully Added")
    
    dept_data = DepartmentModel.objects.all()

    context = {
        'dept_data':dept_data
    }

    return render(request, 'pages/addDepartment.html',context)

def edit_Deptpage(request,id):
    if request.method == "POST":
        name = request.POST.get("dept_name")

        DepartmentModel(
            id=id,
            name = name
        ).save()

        messages.success(request, "Department Successfully Edited")
        return redirect('addDepartment')
    
    dept_data = DepartmentModel.objects.get(id=id)

    context = {
        'data':dept_data
    }

    return render(request, 'pages/editDepartment.html',context)

def addDoctorPage(request):
    if request.method == "POST":
        name = request.POST.get('doctor_name')
        specialization = request.POST.get('specialization')
        doctor_email = request.POST.get('doctor_email')
        dept_id = request.POST.get('dept_id')

        dept_obj = DepartmentModel.objects.get(id=dept_id)

        DoctorModel.objects.create(
            name = name,
            specialization = specialization,
            email = doctor_email,
            dept = dept_obj

        )
        messages.success(request, 'Doctor Added')      

    doctor_data = DoctorModel.objects.all()

    dept_data = DepartmentModel.objects.all()
    context ={
        'dept_data': dept_data ,
        'doctor_data': doctor_data ,
    }
    return render(request, 'pages/addDoctor.html', context)


def editDoctorPage(request, id):

    if request.method =="POST":
        name = request.POST.get('doctor_name')
        specialization = request.POST.get('specialization')
        doctor_email = request.POST.get('doctor_email')
        dept_id = request.POST.get('dept_id')

        dept_obj = DepartmentModel.objects.get(id=dept_id)

        DoctorModel(
            id=id,
            name = name,
            specialization = specialization,
            email = doctor_email,
            dept = dept_obj

        ).save()
        messages.success(request, 'Doctor Edited') 
        return redirect('addDoctor')  

    doctor_data = DoctorModel.objects.get(id=id)
    dept_data = DepartmentModel.objects.all()
    context = {
        'doctor_data':doctor_data,
        'dept_data': dept_data
    }
    return render(request,'pages/editDoctor.html',context)

def deleteDoctorPage(request, id):
    DoctorModel.objects.get(id=id).delete()
    return redirect('addDoctor')


def addpatientPage(request):
    if request.method == "POST":
        name = request.POST.get('patient_name')
        age = request.POST.get('age')
        disease = request.POST.get('disease')
        admit_date = request.POST.get('admit_date')
        doctor_id = request.POST.get('doctor_id')

        doctor_obj = DoctorModel.objects.get(id=doctor_id)

        PatientsModel.objects.create(
            name = name,
            age = age,
            disease = disease,
            admitted_date = admit_date,
            doctor = doctor_obj

        )
        messages.success(request, 'Patient Added')      

    patient_data = PatientsModel.objects.all()
    doctor_data = DoctorModel.objects.all()

    context ={
        'patient_data': patient_data ,
        'doctor_data': doctor_data ,
    }
    return render(request, 'pages/addpatient.html', context)


