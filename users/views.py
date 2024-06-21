from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . models import NewUser
from django.db.models.functions import Trim
from django.db.models import Q
from datetime import datetime

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
    obj = get_object_or_404(NewUser, pk=student_id)
    obj.delete()
    return redirect('admin_db')

def approve_clinic(request, id):
    obj = get_object_or_404(NewUser, pk=student_id)
    obj.is_staff = True
    onj.save()
    return redirect('admin_db')