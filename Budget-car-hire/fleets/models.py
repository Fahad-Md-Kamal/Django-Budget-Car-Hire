from django.db import models
from django.conf import settings

from vehicle.models import Vehicle


class Fleet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users_fleet')
    fleet_vehicles = models.ManyToManyField(Vehicle, related_name='fleet_vehicles')
    created_on = models.DateTimeField(auto_now_add=True)
    fleet_start = models.DateTimeField(blank=True, null=True)
    fleet_duration = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.owner.username }'s Fleet no {self.id}"


    def approve(self):
        self.is_approved = not is_approved
        self.save()

    def paid(self):
        self.is_paid = not is_paid
        self.save()



    ## Check on save if the fleet duration is entered for past time?
    
    