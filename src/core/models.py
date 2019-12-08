import os, random, datetime
from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import( AbstractBaseUser, PermissionsMixin)


from PIL import Image
from core.manager import UserManager


def photo_upload(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    username            = instance.username
    date                = datetime.datetime.now().date()
    # Check if the instance have any username
    # if instance.username:
    #     print('Entered Here')
    return f'{username}/profile_pics/{date}-{username}{file_extension}'


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create and Store users to the database
    """

    email               = models.CharField(max_length=255, unique=True)
    username            = models.CharField(max_length=50, unique=True)
    first_name          = models.CharField(max_length=50, blank=True, null=True)
    last_name           = models.CharField(max_length=50, blank=True, null=True)
    is_active           = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    joined_on           = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(default='profile_defaul.png', upload_to= photo_upload)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """
        Return user's email
        """
        return self.username
    
AppUser = get_user_model()
class Blog(models.Model):
    """ Stores and Retrieves Blogs of Database"""
    OT  = 0
    VH  = 1
    SV  = 2
    BLOG_TOPICS = [
        (OT, 'OTHERS'),
        (VH, 'VEHICLES'),
        (SV, 'SERVICES'),
        ]
    user                = models.ForeignKey( AppUser, on_delete = models.CASCADE)
    title               = models.CharField(max_length=250)
    content             = models.TextField(max_length=600)
    topic               = models.IntegerField(choices=BLOG_TOPICS, default=OT)
    posted_on           = models.DateTimeField(auto_now_add=True)
    updated_on          = models.DateTimeField(auto_now=True)
    is_approved         = models.BooleanField(default=False)

    def __str__(self):
        return self.title