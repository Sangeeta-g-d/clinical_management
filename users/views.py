from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from users.models import NewUser

# Create your views here.


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
                return redirect('') 
            else:
                error_message = "Invalid username or password."
                messages.error(request, error_message)
                return render(request, 'clinic_login.html')
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'clinic_login.html')
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
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, "clinic_register.html")

        user = NewUser.objects.create(first_name = first_name, phone_no = phone_no, username = username, email = email, password = passw,city=city,address=address,user_type='clinic')
        return redirect('clinic_login')
    return render(request,'clinic_register.html')