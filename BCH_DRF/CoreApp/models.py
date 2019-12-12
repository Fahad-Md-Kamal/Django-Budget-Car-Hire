import datetime, os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from PIL import Image

from CoreApp.manager import UserManager


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    date = datetime.datetime.now()
    return f'profile_pics/{instance.username}/{date}-{username}{file_extension}'



class User(AbstractBaseUser, PermissionsMixin):
    email                   = models.EmailField(max_length=255, unique=True)
    username                = models.CharField(max_length=255, unique=True)
    first_name              = models.CharField(max_length=50, null=True)
    last_name               = models.CharField(max_length=50, null=True)
    # image                   = models.ImageField(default='ProPic.png', upload_to=photo_path, blank=True, null=True)
    is_owner                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD          = 'email'
    REQUIRED_FIELDS         = ['username']


    def __str__(self):
        return self.username


class ProfilePics(models.Model):
    user                    = models.ForeignKey(User, 
                                                on_delete = models.SET_NULL, 
                                                related_name= 'profile_pic',
                                                null= True)
    image                   = models.ImageField(default='ProPic.png', upload_to=photo_path)
    is_approved             = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
