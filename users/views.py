from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . models import Appointments, NewUser, AppointmentTimings, Rating
from . models import Appointments, NewUser, AppointmentTimings,Prescription
from django.db.models.functions import Trim
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse

from users.models import NewUser



def patient_logout(request):
    logout(request)
    return redirect('/patient_login')


def clinic_logout(request):
    logout(request)
    return redirect('/clinic_login')


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
    clinics=NewUser.objects.filter(user_type='clinic')
    return render(request,'patient_db.html', {'clinics':clinics})

def book_appointment(request):
    clinics=NewUser.objects.filter(user_type='clinic')
    return render(request,'book_appointment.html',{'clinics':clinics})

def doctor_appo(request, id):
    patient_id = request.user.id
    clinic_id = id
    doctors = NewUser.objects.filter(user_type='doctor', added_by=id)
    print(patient_id, clinic_id)
    
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        doctor = NewUser.objects.get(id=doctor_id)  # Retrieve the doctor instance
        appointment = Appointments(
            clinic_id=clinic_id,
            patient_id=request.user,
            doctor_id=doctor,  # Assign the doctor instance
            timings=timezone.now()
        )
        appointment.save()

    return render(request, 'doctor_appo.html', {'doctors': doctors})

def appointment_list(request):
    clinic_id = request.user.id
    appointments = Appointments.objects.filter(clinic_id=clinic_id).select_related('doctor_id','patient_id')

    context = {
        'data': appointments
    }

    return render(request, 'appointment_list.html', context)


def doctor_login(request):
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
            return redirect('doctor_db')
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            
            return render(request, 'doctor_login.html',{'error_message':error_message})
    else:
        return render(request, 'doctor_login.html')
    
def doctor_db(request):
    return render(request,'doctor_db.html')
    
def set_timing(request, app_id):
    # Fetch the specific appointment by ID
    obj = get_object_or_404(Appointments.objects.select_related('patient_id', 'doctor_id'), id=app_id)
    
    # Extract doctor ID
    doctor_id = obj.doctor_id.id

    # Fetch timings related to the doctor's appointments
    selected_timings = AppointmentTimings.objects.filter(appo_id__doctor_id=doctor_id)

    if request.method == "POST":
        timing = request.POST.get('timing')
        date = request.POST.get('a_date')
        obj.slot = True
        obj.save()
        new_timing = AppointmentTimings.objects.create(slot_timing=timing, appo_id=obj, date=date)

    context = {
        'obj': obj,
        'selected_timings': selected_timings,
    }
    return render(request, 'set_timing.html', context)



def doctor_login(request):
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
            return redirect('doctor_db')
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            
            return render(request, 'doctor_login.html',{'error_message':error_message})
    else:
        return render(request, 'doctor_login.html')
    
def doctor_db(request):
    patients = AppointmentTimings.objects.select_related('appo_id').filter(appo_id__doctor_id = request.user.id)
    print(patients)
    context = {
        'patients':patients
    }
    return render(request,'doctor_db.html',context)

def add_prescription(request):
    if request.method == 'POST':
        appo_id = request.POST.get('appo_id')
        prescription_text = request.POST.get('prescription')
        print("*****************************************************88",appo_id)
        # Assuming appo_id is an integer
        appointment = Appointments.objects.get(id=appo_id)
        
        # Create Prescription object
        prescription = Prescription.objects.create(
            appo_id=appointment,
            prescription=prescription_text
        )
        
        # Optionally, you can add any additional logic here (e.g., redirect to a success page)
        return redirect('/doctor_db')  # Replace 'appointments_list' with your actual URL name for the appointments list page
    
    return redirect('appointments_list')  # Redirect back to appointments list if not a POST request

def doctor_prescription(request):
    data = Prescription.objects.select_related('appo_id__doctor_id').filter(appo_id__patient_id=request.user.id)
    
    # Fetch ratings for the prescriptions
    ratings = Rating.objects.filter(patient=request.user, prescription__in=data).select_related('prescription')
    ratings_dict = {rating.prescription_id: rating for rating in ratings}

    if request.method == "POST":
        prescription_id = request.POST.get('prescription_id')
        rating_value = request.POST.get('rating')
        
        if prescription_id and rating_value:
            prescription = Prescription.objects.get(id=prescription_id)
            patient = request.user
            doctor = prescription.appo_id.doctor_id

            # Create or update the Rating object
            rating, created = Rating.objects.update_or_create(
                prescription=prescription,
                patient=patient,
                defaults={'doctor': doctor, 'rating': rating_value, 'date': timezone.now()}
            )
            return redirect('doctor_prescription')  # Redirect to the same page or another page

    return render(request, 'doctor_prescription.html', {'data': data, 'ratings_dict': ratings_dict})