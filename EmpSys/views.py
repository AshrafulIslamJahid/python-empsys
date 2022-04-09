
from pickle import TRUE
from django.shortcuts import render,redirect
from django.contrib import messages
from EmpSys.models import Newemployee, Newuser


def IndexPage(request):
    if 'Auth' in request.session:
        return redirect('dashboard')
    return render(request, "index.html")

def Dashboard(request):
    if 'Auth' not in request.session:
        return redirect("login")
    Employees = Newemployee.objects.all()
    return render(request, "dashboard.html", {'Employees': Employees})

def Login(request):
    if 'Auth' in request.session:
        return redirect('dashboard')

    if request.method == 'POST':
        Email = request.POST['email']
        Password = request.POST['password']
        try:
            Newuser.objects.get(Email=Email, Pwd=Password)
            request.session['Auth'] = True
            request.session['Email'] = Email
            return redirect('dashboard')
        except Newuser.DoesNotExist as e:
            messages.success(request, "Wrong Credentials")
            return render(request, "login.html")
    else:
        return render(request, 'login.html')

def Register(request):
    if "Auth" in request.session:
        return redirect('dashboard')
    if request.method == 'POST':
        Username = request.POST['name']
        Email = request.POST['email']
        Pwd = request.POST['password']
        Newuser(Username=Username,Email=Email,Pwd=Pwd).save()
        messages.success(request, "Registration Successful")
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout(request):
    del request.session['Auth']
    return redirect("index")



def createEmp(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Address = request.POST['address']
        Phone = request.POST['phone']
        Newemployee(Name=Name,Address=Address,Phone=Phone).save()
        messages.success(request, "Created Successfully")
        return redirect('dashboard')
    else:
        return render(request, "employee/create.html")
    

def editEmp(request):
    return render(request, "employee/edit.html")