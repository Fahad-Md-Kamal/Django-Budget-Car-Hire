from django.db import models
from django.urls import reverse_lazy
from users.models import Profile
from fleet.models import Fleet


class Transaction(models.Model):
    profile         = models.ForeignKey(Profile, 
                                        on_delete= models.CASCADE, 
                                        related_name='fleet_payer')
    token           = models.CharField(max_length=120)
    fleet           = models.ForeignKey(Fleet, 
                                        on_delete = models.SET_NULL, 
                                        blank=True, 
                                        null=True, 
                                        related_name= 'paid_fleet')
    amount          = models.DecimalField(max_digits=100, 
                                        decimal_places=2)
    success         = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True, 
                                            auto_now=False)


    class Meta:
        ordering    = ['-timestamp']


    def __str__(self):
        return self.fleet.fleet_ref

