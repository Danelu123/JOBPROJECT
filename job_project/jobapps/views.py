# jobapps views file

from django.shortcuts import render,redirect
from .forms import JobForm1
from django.contrib import messages
from .models import JobFields


def Upload_View1(request):
    if request.method == 'POST':
        form = JobForm1(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            messages.success(request,'Job Uploaded Successfully...')
            return redirect('Home2')
        else:
            # messages.warning(request, 'Something went wrong...')
            form = JobForm1()
            return render(request, 'jobapp/upload_job2.html', {'form': form})
    else:
        form = JobForm1()
        return render(request, 'jobapp/upload_job2.html', {'form': form})

def Job_View1(request):
    form = JobFields.objects.all()
    return render(request,'jobapp/job_view.html',{'form':form})

def Job_View2(request,id):
    form = JobFields.objects.filter(id=id)
    return render(request,'jobapp/job_view1.html',{'form':form})