from django import forms
from hsp.models import *
from django.core import validators

class patientForm(forms.ModelForm):
    class Meta:
        model=patientdatamodel
        fields=['name','email','mobileno','gender','weight','age','symptomps','doctor','file']







