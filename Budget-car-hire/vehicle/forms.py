from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from . import models





class vehicle_reg_form(forms.ModelForm):

    reg_no = forms.CharField(
        label = 'Registration no: ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reg No'}))


    model_name = forms.CharField(
        label = 'Vehicle model: ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reg No'}))

    class Meta:
        model = models.Vehicle
        fields = ('reg_no', 'model_name', 'vehicle_type')


        widgets = {
            'reg_no': forms.TextInput(
                    attrs=
                    {'class':'form-control', 'placeholder':'Reg No: VMX 19654'}),
            'model_name': forms.TextInput (attrs=
                    {'class':'form-control', 'placeholder': 'Model Name: e.g Ford Mustung'})
        }
