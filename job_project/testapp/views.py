# testapp views file

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Home_page(request):
    return render(request,'testapp/Home_page.html')
def Home_page1(request):
    return render(request,'testapp/Home1.html')

def Home_page2(request):
    return render(request,'testapp/Home2.html')