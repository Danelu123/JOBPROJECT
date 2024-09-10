# API1 Views file

from rest_framework.viewsets import ModelViewSet
from jobapps.models import JobFields
from jobapps.api1.serializer import JobSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication

class Job_View(ModelViewSet):
    queryset = JobFields.objects.all()
    serializer_class = JobSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]