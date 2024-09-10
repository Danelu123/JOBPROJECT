# API2 Views file

from rest_framework.viewsets import ModelViewSet
from fieldsapp.models import Profile
from fieldsapp.api2.serializer import Profile_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication

class Profile_View(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profile_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]