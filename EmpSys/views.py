
from pickle import TRUE
from django.shortcuts import render
from django.contrib import messages
from EmpSys.models import Newuser


def IndexPage(request):
    return render(request, "index.html")

def Dashboard(request):
    return render(request, "dashboard.html")

def Login(request):
    if request.method == 'POST':
        Email = request.POST['email']
        Password = request.POST['password']
        try:
            Newuser.objects.get(Email=Email, Pwd=Password)
            request.session['Auth'] = TRUE
            return render(request, 'dashboard.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, "Wrong Credentials")
            return render(request, "login.html")
    else:
        return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        Username = request.POST['name']
        Email = request.POST['email']
        Pwd = request.POST['password']
        Newuser(Username=Username,Email=Email,Pwd=Pwd).save()
        messages.success(request, "Registration Successful")
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

        