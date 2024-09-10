# userapp urls file

from django.urls import path
from .views import Applicant_View,Login_View1,Login_View2,Recruiter_View

urlpatterns = [
    path('appli', Applicant_View, name='appli'),
    path('rec', Recruiter_View, name='rec'),
    path('login1', Login_View1, name='login1'),
    path('login2', Login_View2, name='login2'),
]
