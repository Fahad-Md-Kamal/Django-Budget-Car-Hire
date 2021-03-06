# Deleveoped
# Fahad Md Kamal
# NCC ID: 00171328

from django.db import models
from django.urls import reverse_lazy
from datetime import datetime, timedelta

from vehicle.models import Vehicle
from users.models import Profile


class Fleet(models.Model):
    user                = models.ForeignKey(Profile, related_name='fleet_owner', on_delete=models.SET_NULL, blank=True, null=True)
    fleet_ref           = models.CharField(max_length=30)
    booked_date         = models.DateTimeField(auto_now_add=True)
    vehicles            = models.ManyToManyField(Vehicle, related_name='fleet_vehicle')
    is_purchased        = models.BooleanField(default=False)
    is_approved         = models.BooleanField(default=False)
    is_freezed          = models.BooleanField(default=False)
    approved_on         = models.DateTimeField(blank=True, null=True)

    def get_fleet_vehicles(self):
        return self.vehicles.all()

    def get_total(self):
        return sum([car.rent for car in self.vehicles.all()])

    def check_hired(self):
        for car in (self.vehicles.all()):
            if car.is_hired:
                return True
        return False

    def duration_check(self):
        return abs((datetime.now() - self.approved_on ).days)

    def expiration_date(self):
        return self.approved_on + timedelta(days=30)


    def approve(self):
        self.is_approved    = not self.is_approved
        self.approved_on    = datetime.now()
        self.save()

    def purchased(self):
        self.is_purchased    = not self.is_purchased
        self.save()

 
    def get_absolute_url(self):
        return reverse_lazy('fleet:detail_fleet', kwargs={'pk': self.pk})


    def __str__(self):
        return self.fleet_ref 



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
    is_purchased    = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True, 
                                            auto_now=False)


    class Meta:
        ordering    = ['-timestamp']

    def __str__(self):
        return self.fleet

