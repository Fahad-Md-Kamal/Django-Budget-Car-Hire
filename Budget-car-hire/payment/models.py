from django.db import models

from fleets.models import Fleet

class FleetPayment(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE, related_name='payment_fleet')
    paid_amount = models.PositiveIntegerField(default=0)
    paid_on = models.DateField(auto_now_add=True)
    is_verified = models.BooleanField(default= False)