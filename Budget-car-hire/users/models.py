from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=20)
    road = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    image = models.ImageField(default='default.png', upload_to ='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'