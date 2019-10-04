from django.core.signals import request_started
from django.conf import settings

from .models import Fleet
from datetime import datetime

def checkdate(sender, **kwargs):
    fleets   = Fleet.objects.all()

    # Checks for all Fleets and their approval date. 
    # If it is 30 day it automatically sets False to is_approval of the fleet and to is_purchased parameter
    for fleet in fleets:
        if fleet.is_approved and fleet.duration_check() > 30:
            fleet.is_approved = False
            fleet.is_purchased = False
            fleet.save()

request_started.connect( checkdate)
