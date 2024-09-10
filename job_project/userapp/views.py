# userapp views file

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User
from .forms import RegisterUserForm


# Applicant view
def Applicant_View(request):
    type = 'app'
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.is_applicant = True
            var.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login1')
        else:
            return redirect('applicant')
    else:
        form = RegisterUserForm()
        return render(request, 'userapp/signup.html', {'form': form,'type':type})

# Recruiter View
def Recruiter_View(request):
    type='rec'
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.is_recruiter = True
            var.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login2')
        else:
            messages.warning(request, 'Please correct the error(s) below:')
            return redirect('recruiter')

    else:
        form = RegisterUserForm()
        return render(request, 'userapp/signup.html', {'form': form,'type':type})

# Applicant Login View
def Login_View1(request):
    type='app'
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request, 'Successfully Login...')
            return redirect('Home1')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('login1')
    else:
        return render(request,'userapp/login.html',{'type':type})

# Recruiter Login View
def Login_View2(request):
    type='rec'
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('Home2')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('login2')
    else:
        return render(request,'userapp/login.html',{'type':type})

