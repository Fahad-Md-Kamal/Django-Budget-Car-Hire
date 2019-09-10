from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

from vehicle.models import Vehicle


class Fleet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users_fleet')
    fleet_vehicles = models.ManyToManyField(Vehicle, related_name='fleet_vehicles')
    created_on = models.DateTimeField(auto_now_add=True)
    fleet_start = models.DateTimeField(blank=True, null=True)
    fleet_duration = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_freezed = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True)


    def __str__(self):
        return f"{self.owner.username }'s Fleet no {self.id}"

    @staticmethod
    def approve(self):
        self.is_approved = not self.is_approved
        self.save()

    @staticmethod
    def freezed(self):
        self.is_freezed = not self.is_freezed
        self.save()

    def paid(self):
        self.is_paid = not is_paid
        self.save()


    @staticmethod
    def get_fleet_total(self):
        return sum([Vehicle.rent_per_month for Vehicle in self.fleet_vehicles.all()])


    @staticmethod
    def get_fleet_vehicle(self):
        return self.fleet_vehicles.all()


    def get_absolute_url(self):
        return reverse_lazy('fleets:fleet_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['is_approved',]

    ## Check on save if the fleet duration is entered for past time?