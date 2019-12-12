from django.db.models.signals import post_save
from django.conf import settings

from CoreApp import models

def create_profile(sender, **kwargs):
    if kwargs['created']:
        models.ProfilePics.objects.create( user=kwargs['instance'] )

post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)


