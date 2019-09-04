from django import forms


from . import models


class DateInputForm(forms.DateTimeInput):
    input_type = 'date'


class FleetRegisterForm(forms.ModelForm):
    
    class Meta:
        model = models.Fleet
        fields = ('fleet_start','fleet_duration')

        widgets = {
            'fleet_start': DateInputForm(),
            'fleet_duration': DateInputForm(),
        }
    