#pylint: disable = no-member, unused-variable

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
import os, random, datetime
from PIL import Image


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    username = instance.user.username
    date = datetime.datetime.now()
    return f'profile_pics/{instance.user.id}/{date}-{username}{file_extension}'


class Profile(models.Model):

    CU    = 0
    OW    = 1

    USER_CATEGORY = (
        (CU, 'CUSTOMER'),
        (OW, 'OWNER'),
    )


    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    house       = models.CharField(max_length=20)
    road        = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=20)
    user_type   = models.IntegerField(choices=USER_CATEGORY, default=CU)
    image       = models.ImageField(default='default_profile.png', upload_to =photo_path)
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender= settings.AUTH_USER_MODEL)