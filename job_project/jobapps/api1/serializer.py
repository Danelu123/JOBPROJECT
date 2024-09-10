# API1 Serializer File
from rest_framework.serializers import ModelSerializer
from jobapps.models import JobFields

class JobSerializer(ModelSerializer):
    class Meta:
        model = JobFields
        fields = '__all__'