#pylint: disable = no-member, unused-variable

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import os, random, datetime
from PIL import Image



def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    print(basefilename, file_extension)
    vehicle_reg = instance.reg_no
    date = datetime.datetime.now()
    return f'vehicle_pics/{vehicle_reg}/{date}-{vehicle_reg}{file_extension}'



class Vehicle(models.Model):
    SM = 0
    MD = 1
    LG = 2
    VN = 3
    VEHICLE_CATEGORIES = [
        (SM, 'Small'),
        (MD, 'Medium'),
        (LG, 'Large'),
        (VN, 'Van'),
    ]

    VEHICLE_MODEL = [
        ( 0, 'Other'),
        ( 1, 'Audi'),
        ( 2, 'BMW'),
        ( 3, 'Chevrolet'),
        ( 4, 'Ford'),
        ( 5, 'Honda'),
        ( 6, 'Hyundai'),
        ( 7, 'Jeep'),
        ( 8, 'Kia'),
        ( 9, 'Lexus'),
        ( 10, 'Mazda'),
        ( 11, 'Mercedes-Benz'),
        ( 12, 'Mitsubishi'),
        ( 13, 'Nissan'),
        ( 14, 'Renault'),
        ( 15, 'Suzuki'),
        ( 16, 'Subaru'),
        ( 17, 'Tata'),
        ( 18, 'Toyota'),
        ( 19, 'VolksWagen'),
        ( 20, 'Volvo'),
    ]

    owner           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicel_owner')
    model_name      = models.IntegerField(choices=VEHICLE_MODEL, default=0)
    model_year      = models.DateField(blank=True, null=True)
    reg_no          = models.CharField(max_length=20, unique=True)
    vehicle_type    = models.IntegerField(choices=VEHICLE_CATEGORIES, default=SM)
    added_on        = models.DateField(auto_now_add=True)
    rent            = models.PositiveIntegerField(default = 2000)
    capacity        = models.PositiveIntegerField(default=2)
    is_freezed      = models.BooleanField(default=False)
    is_approved     = models.BooleanField(default=False)
    is_booked       = models.BooleanField(default=False)
    booked_date     = models.DateTimeField( auto_now=True, blank=True, null=True)
    is_hired        = models.BooleanField(default=False)
    image           = models.ImageField(default='default_vehicle.png', upload_to =photo_path)

    class Meta:
        ordering = ['-is_approved',]


    def get_absolute_url(self):
        return reverse_lazy('vehicle:detail_vehicle', kwargs={'pk': self.pk})


    def approve_vehicle(self):
        self.is_approved = not self.is_approved
        self.save()

    def freeze_vehicle(self):
        self.is_freezed = not self.is_freezed
        self.save()


    def save(self, *args, **kwargs):
        super(Vehicle, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 350:
            output_size = (400, 450)
            img.thumbnail(output_size)
            img.save(self.image.path)


    @staticmethod
    def hire_vehicle(self):
        self.is_hired = not self.is_hired
        self.save()


    @staticmethod
    def booked(self):
        self.is_booked  = True
        self.booked_date = datetime.datetime.now()
        self.save()

    @staticmethod
    def unbook(self):
        self.is_booked  = False
        self.booked_date = datetime.datetime.now()
        self.save()


    def __str__(self):
        return  self.reg_no
        

