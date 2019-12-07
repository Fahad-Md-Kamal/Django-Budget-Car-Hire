import os, random, datetime
from django.db import models
from django.contrib.auth.models import( AbstractBaseUser, PermissionsMixin)

from PIL import Image
from core.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create and Store users to the database
    """

    email               = models.CharField(max_length=255, unique=True)
    username            = models.CharField(max_length=50, unique=True)
    first_name          = models.CharField(max_length=50, blank=True, null=True)
    last_name           = models.CharField(max_length=50, blank=True, null=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=True)
    joined_on           = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """
        Return user's email
        """
        return self.email
    
