# Jobapps urls file

from django.urls import path,include
from .views import Upload_View1,Job_View1,Job_View2

urlpatterns = [
    path('upload1',Upload_View1,name='upload1'),
    path('job1', Job_View1, name='job1'),
    path('job2/<int:id>/', Job_View2,),

]