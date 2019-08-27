from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=20)
    road = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    image = models.ImageField(default='default.png', upload_to ='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)