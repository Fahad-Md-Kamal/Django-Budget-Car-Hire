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
    added_on = models.DateField(auto_now_add=True)
    rent_per_month = models.PositiveIntegerField(default = 2000)
    capacity = models.PositiveIntegerField(default=2)
    is_freezed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_hired = models.BooleanField(default=False)


    class Meta:
        ordering = ['vehicle_type',]


    def get_absolute_url(self):
        return reverse_lazy('vehicle:detail_vehicle', kwargs={'pk': self.pk})


    def approve_vehicle(self):
        self.is_approved = not self.is_approved
        self.save()

    def delete_vehicle(self):
        self.delete()

    def freeze_vehicle(self):
        self.is_freezed = not self.is_freezed
        self.save()


    def hire_vehicle(self):
        self.is_hired
        self.save()


    def __str__(self):
        return  self.model_name + '  ' + self.reg_no
        
        