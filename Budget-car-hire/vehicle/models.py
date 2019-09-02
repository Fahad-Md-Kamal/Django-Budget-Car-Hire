from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Vehicle(models.Model):
    SM = 0
    MD = 1
    LG = 2
    VN = 3
    VEHICLE_CATEGORIES = [
        (SM, 'Small Car'),
        (MD, 'Medium Car'),
        (LG, 'Large Car'),
        (VN, 'Van'),
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicel_owner')
    model_name = models.CharField(max_length=20,)
    model_year = models.DateField(blank=True, null=True)
    reg_no = models.CharField(max_length=20, unique=True)
    vehicle_type = models.IntegerField(choices=VEHICLE_CATEGORIES, default=SM)
    added_on = models.DateField(auto_now=True)
    rent_per_month = models.PositiveIntegerField(default = 2000)
    is_freezed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_hired = models.BooleanField(default=False)


    class Meta:
        ordering = ['vehicle_type',]


    def get_absolute_url(self):
        return reverse_lazy('vehicle:detail_vehicle', kwargs={'pk': self.pk})


    def approve_vehicle(self):
        self.is_approved = True
        self.save()


    def freez_vehicle(self):
        self.is_freezed = True
        self.save()


    def hire_vehicle(self):
        self.is_hired = True
        self.save()


    def __str__(self):
        return self.reg_no
        
        