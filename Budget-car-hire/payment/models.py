from django.db import models

from fleets.models import Fleet

class FleetPayment(models.Model):

    CASH = 0
    NAGAD = 1
    BANK_TRANS = 2
    VISA = 3
    MASTERCARD = 4
    AMERICAN_EXPRESS = 5

    PAYMENT_METHOD = (
        (CASH, 'Direct Payment'),
        (NAGAD, 'Nagad App-pay'),
        (BANK_TRANS, 'Bank Transection'),
        (VISA, 'VISA Payment'),
        (MASTERCARD, 'MASTERCARD Payment'),
        (AMERICAN_EXPRESS, 'AMERICAN EXPRESS'),
    )

    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE, related_name='payment_fleet')
    payment_medium = models.IntegerField(choices= PAYMENT_METHOD, default= CASH)
    paid_amount = models.PositiveIntegerField(default=0)
    paid_on = models.DateField(auto_now_add=True)
    transection_id = models.CharField(max_length=50, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True, )
    is_verified = models.BooleanField(default= False)