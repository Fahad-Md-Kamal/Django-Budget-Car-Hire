from django import forms
from . import models





class vehicle_reg_form(forms.ModelForm):

    
    
    reg_no = forms.TextInput()
    model_name = forms.TextInput()
    vehicle_type = forms.IntegerField()


    class Meta:
        model = models.Vehicle
        fields = ('reg_no', 'model_name', 'vehicle_type')


        # widgets = {
        #     'reg_no': forms.TextInput(attrs=
        #             {'class':'form-control', 'placeholder':'Blog Title'}),
        #     'model_name': forms.TextInput (attrs=
        #             {'class':'form-control', 'placeholder': 'Max 600 words'}),
        #     'vehicle_type': forms.ChoiceField(
        #         label = "Vehicle Type",
        #         widgets = forms.Select(choices = VEHICLE_CATEGORIES))
        # }
