from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views import generic
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from . import forms, models
from fleet.models import Fleet

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# def checkout(request, pk):
#     template                        = 'payment/payment_user.html'

#     fleet_to_pay                    = get_object_or_404(Fleet, pk = pk)
#     publish_key                     = settings.STRIPE_PUBLISHABLE_KEY
#     if request.method               == 'POST':
#         token = request.POST.get['stripeToken', False]
#         print(token)
#         try:
#             charge = stripe.Charge.create(
#                 amount = fleet_to_pay.get_total(),
#                 currency = 'usd',
#                 description = 'Example charge',
#                 source = token,
#                 # capture=False,
#             )
#             fleet_to_pay.is_purchased   = True
#             fleet_to_pay.booked_date    = datetime.now()
#             fleet_to_pay.save()

#             fleet_vehicles              = fleet_to_pay.vehicles.all()
#             fleet_vehicles.Update(is_booked = Flase, is_hired = True)

#             transection                 = models.Transaction(profile = request.user.profile,
#                                                             fleet = fleet_to_pay,
#                                                             amount = fleet_to_pay.get_total(),
#                                                             token = token,
#                                                             is_purchased = True)
#             transection.save()

#             messages.info(request, 'Your payment has been done successfully')
#             return HttpResponseRedirect(fleet_to_purchase.get_absolute_url())
#             # return redirect(reverse('payment:update_payment_record', kwargs= {'token': token}))
        
#         except stripe.CardError as e:
#             messages.info(request, 'Couldn\'t complete the request')

#     return render(request, template, {})
     
     

def update_payment_record(request, token):

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
    transaction = models.Transaction( profile        = request.user.profile,
                                      fleet           = fleet_to_purchase,
                                      amount          = fleet_to_purchase.get_total(),
                                      is_purchased    = True )
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