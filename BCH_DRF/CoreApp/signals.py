from django.db.models.signals import post_save
from django.conf import settings

from CoreApp.models import Vehicle, VehiclePics


def create_profile(sender, **kwargs):
    if kwargs['created']:
        VehiclePics.objects.create(vehicle=kwargs['instance'])
post_save.connect(create_profile, sender=Vehicle)

