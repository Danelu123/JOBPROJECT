# API1 urls file

from django.urls import path, include
from jobapps.api1.views import Job_View
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'jobs', Job_View)

urlpatterns = [
    path('', include(router.urls)),

]
