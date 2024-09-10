# jobapps forms file

from django import forms
from .models import JobFields

class JobForm1(forms.ModelForm):
    class Meta:
        model = JobFields
        fields = '__all__'