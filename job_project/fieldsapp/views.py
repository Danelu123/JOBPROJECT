# # fieldsapp views file

from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

def Profile_View(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            messages.success(request,'Successfully Applied...')
            return redirect('job1')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('profile')
    else:
        form = ProfileForm()
        return render(request,'fieldsapp/profile1.html',{'form':form})


