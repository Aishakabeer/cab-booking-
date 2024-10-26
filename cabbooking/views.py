from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from User.models import User_tbl,Vehicle


# Create your views here.
def index(request):
    return render(request, 'index.html')  # Render the index.html template

def contacts(request):
    return render(request, 'contact.html')



def logoutt(request):
    if 'user' in request.session:
        request.session.flush()
    logout(request)
    if 'phone' in request.session:
        request.session.flush()
    logout(request)
    return redirect('index')

def loginn(request):
    if 'user' in request.session:
        return redirect('/User')
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User_tbl.objects.filter(phonenumber=phone, password=password,role="user").last()
        if user is not None:
            request.session['user'] = phone
            return redirect('/User')
        else:
            return HttpResponse("signupfirst")
    return render(request, 'login.html')

def signupp(request):
    if request.method == "POST":
        saverecords = User_tbl()
        saverecords.name = request.POST.get('name')
        saverecords.address = request.POST.get('address')
        saverecords.email_id = request.POST.get('email')
        saverecords.phonenumber = request.POST.get('phone')
        saverecords.password = request.POST.get('password')
        saverecords.role = 'user'
        saverecords.save()
        return redirect('loginn')
    return render(request, 'signup.html')

def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "admin":
            return redirect('/Admins/')
        else:
            return HttpResponse("Invalid credentials, please try again.")
    return render(request, 'adminlogin.html')
