from django.db import models

from vehicle.models import Vehicle
from users.models import Profile

# class Fleet_Vehicle(models.Model):
#     vehicle         = models.OneToOneField( Vehicle, on_delete=models.SET_NULL, blank=True, null=True)
#     is_hired        = models.BooleanField(default=False)
#     date_booked     = models.DateTimeField(auto_now=True)
#     date_hired      = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.vehicle.reg_no


class Fleet(models.Model):
    customer        = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    vehicles        = models.ManyToManyField(Vehicle, blank=True, null=True)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated         = models.DateTimeField(auto_now= True)
    date_booked     = models.DateTimeField(auto_now_add= True)

    def get_fleet_vehicles(self):
        return self.vehicles.all()

    def get_fleet_total(self):
        return sum([car.vehicle.rent for car in self.vehicles.all()])

    def __str__(self):
        return str(self.id)