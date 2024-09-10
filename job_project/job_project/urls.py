"""
URL configuration for job_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from userapp import views as user
from testapp import views as test
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),

    # User-related views
    path('applicant/', user.Applicant_View, name='applicant'),
    path('recruiter/', user.Recruiter_View, name='recruiter'),
    path('login1/', user.Login_View1, name='login1'),
    path('login2/', user.Login_View2, name='login2'),

    # Testapp views
    path('', test.Home_page),
    path('Home1/', test.Home_page1, name='Home1'),
    path('Home2/', test.Home_page2, name='Home2'),

    # Job-related URLs
    path('', include('jobapps.urls')),
    path('api1/', include('jobapps.api1.urls')),

    # Profile-related URLs
    path('profile/', include('fieldsapp.urls')),
    path('api2/', include('fieldsapp.api2.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    # Token-based Authentication URLs
    path('auth-jwt/',obtain_jwt_token),
    path('auth-jwt-refresh/',refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]

