from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . models import NewUser
from django.db.models.functions import Trim
from django.db.models import Q
from datetime import datetime


from users.models import NewUser

# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None and user.is_superuser == True:
            login(request,user)
            return redirect('/admin_db')
        else:
            error_message = "Invalid username or password"
            return render(request,'admin_login.html',{'error_message':error_message})
    return render(request,'admin_login.html')

def admin_db(request):
    search_query = request.GET.get('search', '')
    data = NewUser.objects.filter(user_type='clinic')
    if search_query:
        data = data.filter(
            Q(first_name__icontains=search_query) 
        )
    context = {
        'data':data
    }
    return render(request,'admin_db.html',context)

def delete_clinic(request, id):
    obj = get_object_or_404(NewUser, pk=id)
    obj.delete()
    return redirect('admin_db')

def approve_clinic(request, id):
    obj = get_object_or_404(NewUser, pk=id)
    obj.is_staff = True
    obj.save()
    return redirect('admin_db')

def admin_logout(request):
    logout(request)
    return redirect('/admin_login')


def clinic_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #user_type = request.user.user_type
        print(username,password,user)
        #print("hiii",user_type,username)
        if user is not None:
            if user.is_staff:
                login(request, user)
            # Redirect to a success page.
                return redirect('/clinic_db') 
            else:
                error_message = "Wait till account varifies"
                
                return render(request, 'clinic_login.html',{'error_message':error_message})
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            
            return render(request, 'clinic_login.html',{'error_message':error_message})
    else:
        return render(request, 'clinic_login.html')
    

def clinic_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('clinic_name')
        phone_no = request.POST.get('phone_no')
        username = request.POST.get('username')
        city = request.POST.get('city')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passw = make_password(password)
        if NewUser.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different username'
            return render(request, "clinic_register.html", {'error_message':error_message})

        user = NewUser.objects.create(first_name = first_name, phone_no = phone_no, username = username, email = email, password = passw,city=city,address=address,user_type='clinic')
        return redirect('clinic_login')
    return render(request,'clinic_register.html')


def clinic_db(request):
    data = NewUser.objects.filter(user_type='doctor', added_by = request.user.id)
    context = {
        'data':data
    }
    print(request.user.id)
    return render(request,'clinic_db.html',context)

def add_doctor(request):
    success = False
    if request.method == 'POST':
        qualification = request.POST.get('quali')
        specialization = request.POST.get('speci')
        username = request.POST.get('username')
        phone_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        available_timimg = request.POST.get('timing')
        city=request.POST.get('city')
        first_name=request.POST.get('doctor')
        if NewUser.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different username'
            return render(request, "add_doctor.html", {'error_message':error_message})

        passw = make_password(phone_no)
        user = NewUser.objects.create(qualification = qualification, phone_no = phone_no, username = username, email = email, specialization = specialization,available_timings=available_timimg,user_type='doctor',city=city,first_name=first_name, password=  passw,added_by=request.user.id)
    return render(request,'add_doctor.html')

def edit_doc_info(request,id):
    obj = NewUser.objects.get(id=id)
    if request.method == 'POST':
        obj.qualification = request.POST.get('quali')
        obj.specialization = request.POST.get('speci')
        obj.username = request.POST.get('username')
        obj.phone_no = request.POST.get('contact_no')
        
        obj.email = request.POST.get('email')
        obj.available_timings = request.POST.get('timing')
        obj.city=request.POST.get('city')
        obj.first_name=request.POST.get('doctor')
        obj.save()
        return redirect('clinic_db')
    return render(request,'edit_doc_info.html',{'obj':obj})


def patient_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        phone_no = request.POST.get('phone_no')
        username = request.POST.get('username')
        city = request.POST.get('city')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passw = make_password(password)
        if NewUser.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different username'
            return render(request, "clinic_register.html", {'error_message':error_message})

        user = NewUser.objects.create(first_name = first_name, phone_no = phone_no, username = username, email = email, password = passw,city=city,address=address,user_type='patient')
        return redirect('patient_login')
    return render(request,'patient_register.html')


def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #user_type = request.user.user_type
        print(username,password,user)
        #print("hiii",user_type,username)
        if user is not None:
            
            login(request, user)
            # Redirect to a success page.
            return redirect('patient_db')
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            
            return render(request, 'patient_login.html',{'error_message':error_message})
    else:
        return render(request, 'patient_login.html')
    
def patient_db(request):
    return render(request,'patient_db.html')

def book_appointment(request):
    clinics=NewUser.objects.filter(user_type='clinic')
    return render(request,'book_appointment.html',{'clinics':clinics})
    

def doctor_appo(request,id):
    doctors=NewUser.objects.filter(user_type='doctor',added_by=id)
    return render(request,'doctor_appo.html',{'doctors':doctors})
    