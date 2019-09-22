from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from . import models



class DateInputForm(forms.DateTimeInput):
    input_type = 'date'


class vehicle_reg_form(forms.ModelForm):

    reg_no = forms.CharField(
        label = 'Registration no: ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. VXN-854'}))
    
    capacity = forms.CharField(
        label = 'Capacity: ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 4 persons'}))
    
    rent = forms.CharField(
        label = 'Rent/month: ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 80000'}))

    class Meta:
        model = models.Vehicle
        fields = ('model_name',
                  'reg_no', 
                  'model_year',
                  'capacity',
                  'rent',
                  'image',
                  'vehicle_type',
                  )

        widgets = {
            'reg_no': forms.TextInput(
                    attrs=
                    {'class':'form-control', 'placeholder':'Reg No: VMX 19654'}),
            'model_year': DateInputForm()
        }
    
