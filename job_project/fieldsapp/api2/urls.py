# API2 urls file

from django.urls import path, include
from fieldsapp.api2.views import Profile_View
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', Profile_View)

urlpatterns = [
    path('', include(router.urls)),

]
