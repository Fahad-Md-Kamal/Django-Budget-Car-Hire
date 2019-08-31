from django.db import models
from django.contrib.auth.models import User




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
    reg_no = models.CharField(max_length=20, unique=True)
    model_name = models.CharField(max_length=20,)
    vehicle_type = models.IntegerField(choices=VEHICLE_CATEGORIES, default=SM)
    is_hired = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    added_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.reg_no

    class Meta:
        ordering = ['vehicle_type',]
        