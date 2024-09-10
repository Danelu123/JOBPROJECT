# testapp urls file
from django.urls import path
from .views import Home_page,Home_page1,Home_page2

urlpatterns = [
    path('', Home_page,),
    path('Home1', Home_page1, name='Home1'),
    path('Home2', Home_page2, name='Home2'),
]
