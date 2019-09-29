from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from . import forms, models
from fleet.models import Fleet

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def make_payment(request):
    template                            = 'payment/payment_user.html'

    return render(request, template, {})
     
     

def update_payment_record(request, fleet_pk):

    fleet_to_purchase                   = get_object_or_404(Fleet, pk = fleet_pk)


    # Fleet property modification
    fleet_to_purchase.is_purchased      = True
    fleet_to_purchase.booked_date       = datetime.now()
    fleet_to_purchase.save()

    # Get all Vehicles of the Fleet
    fleet_vhicles                       = fleet_to_purchase.vehicles.all()

    # Update vehicles property          
    fleet_vhicles.Update( is_booked = False, is_hired= True )

    # create a transaction 
    transaction = models.Transaction(profile        = request.user.profile,
                                    fleet           = fleet_to_purchase,
                                    amount          = fleet_to_purchase.get_total(),
                                    is_purchased    = True
                                        )
    transaction.save()

    # Success message.
    messages.info(request, 'Your payment has been done successfully')
    # Redirecting to the fleet
    return HttpResponseRedirect(fleet_to_purchase.get_absolute_url())
























         # ctx = stripe.PaymentIntent.create(
    # amount=999,
    # currency='usd',
    # payment_method_types=['card'],
    # receipt_email='jenny.rosen@example.com',
    # ) 