from django import forms
from . import models


class FleetPaymentForm(forms.ModelForm):

    card_number = forms.CharField(
        help_text = 'Must be within 16 Charector',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'X123456987'})
    )

    class Meta:
        model = models.FleetPayment
        fields = (
                'payment_medium', 
                'account_name',
                'card_number',
                'transection_id',
                )


        widgets = {
            'transection_id': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Tx854cn541b'}
            ),
            'account_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Owner of the Account'}
            )
        }

      