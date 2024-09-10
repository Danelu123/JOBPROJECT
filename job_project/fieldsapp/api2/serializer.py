# API2 Serializer File
from rest_framework.serializers import ModelSerializer
from fieldsapp.models import Profile

class Profile_Serializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'