from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from uuid import uuid4
from datetime import datetime

from users.models import Profile
from .models import Fleet
from vehicle.models import Vehicle

import stripe


@login_required
def fleet_view(request):
    template                    = 'fleet/fleets.html'
    req_user                    = request.user.user_profile
    fleets                      = Fleet.objects.filter(user = req_user)
    context                     = {
        'fleets': fleets,
    }
    return render(request, template, context)


@login_required
def fleet_detail_view(request, pk, car_pk=None):
    template            = 'fleet/fleet_detail.html'
    fleet               = get_object_or_404(Fleet, pk = pk)
    fleet_id            = request.session.get('fleet_id', None)
    car                 = ''
    if car_pk:
        car                 = get_object_or_404(Vehicle, pk = car_pk)
    # if fleet_id:
        # del request.session['fleet_id']
    context             = {
        'fleet': fleet,
        'vehicles' : fleet.get_fleet_vehicles(),
        'total': fleet.get_total(),
        'car': car
    }
    return render(request, template, context)


@login_required
def existing_fleet(request, pk):
    fleet               = get_object_or_404(Fleet, pk = pk)
    request.session['fleet_id'] = fleet.id
    return redirect('vehicle:vehicle_list')


@login_required
def add_to_fleet(request, pk):
    user                        = request.user.user_profile
    fleet_id                    = request.session.get('fleet_id', None)
    car                         = get_object_or_404(Vehicle, pk = pk)
    fleet                       = ''
    if fleet_id is None:
        fleet = Fleet.objects.create(user = user, fleet_ref = str(uuid4())[-6:].upper())
        fleet.vehicles.add(car)
        car.booked(car)
        messages.info(request, f'{car.reg_no} added to fleet {fleet.fleet_ref}')
        request.session['fleet_id'] = fleet.id
    else:
        fleet                   = get_object_or_404(Fleet, pk = fleet_id)
        if not fleet.user == user:
            messages.error(request, f'You cannot modify this Fleet')
        elif fleet.vehicles.count == 11:
            messages.info(request, f'You have reached the max number vehicle for a fleet')
        else:
            fleet.vehicles.add(car)
            car.booked(car)
            messages.info(request, f'{car.reg_no} added to fleet {fleet.fleet_ref}')
    
    return HttpResponseRedirect(fleet.get_absolute_url())


@login_required
def remove_from_fleet(request, fleet_pk, vehicle_pk):
    car             = get_object_or_404(Vehicle, pk = vehicle_pk)
    fleet           = get_object_or_404(Fleet, pk = fleet_pk)
    if request.user.is_staff or request.user.user_profile == fleet.user:
        fleet.vehicles.remove(car)
        messages.info(request, f'{car.reg_no} removed form the vehicel')
    else:
        messages.error(request, 'You cannot perform vehicle remove action on this fleet')
    return HttpResponseRedirect(fleet.get_absolute_url())


@login_required
def remove_fleet(request, pk):
    fleet           = get_object_or_404(Fleet, pk = pk)
    if request.user.is_staff or request.user.user_profile == fleet.user:
        Fleet.delete(fleet)
        messages.info(request, f'{fleet.fleet_ref} removed')
    else:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())
    return redirect ('fleet:fleets')



def payement_form(request, pk):
    template = 'fleet/checkout.html'
    fleet       = get_object_or_404(Fleet, pk = pk)
    context     = {
        'fleet': fleet,
    }
    return render (request, template, context)

@login_required
def checkout(request, pk):
    template = 'fleet/checkout.html'
    # existing_fleet = fleet_view(request)
    existing_fleet = get_object_or_404(Fleet, pk = pk)

    publishkey  = settings.STRIPE_PUBLISHABLE_KEY
    print(publishkey)
    
    if request.method == 'POST':
        print('Paid')
        try:
            stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY
            number = request.POST['number']
            exp_month = request.POST['month']
            exp_year = request.POST['year']
            cvc = request.POST['cvc']

            if exp_month > datetime.now().month():
                print( puran)

            print(number);
            print(exp_month);

            token = stripe.Token.create(
                card = {
                    'number': number,
                    'exp_month': exp_month,
                    'exp_year': exp_year,
                    'cvc': cvc,
                }
            )

            print(token);

            # charge = stripe.Charge.create(
            #     amount = existing_fleet.get_total(),
            #     currency = 'usd',
            #     description = 'Example charge',
            #     source = token
            # )
            # return redirect(reversed('fleet:update_payment_record',
            #             kwargs = {
            #                 'token':token
            #                 })
            #             )

        except stripe.error.CardError as e:
            messages.info(request, "Your payment request couldn't be completed")

    context = {
        'fleet': existing_fleet,
        'STRIPE_PUBLISHABLE_KEY': publishkey
    }

    return HttpResponseRedirect(existing_fleet.get_absolute_url())


def update_payment_record(request, token):
    fleet_to_purchase                   = get_object_or_404(Fleet, pk = fleet_pk)
    fleet_to_purchase.is_purchased      = True
    fleet_to_purchase.booked_date       = datetime.now()
    fleet_to_purchase.save()
    fleet_vhicles                       = fleet_to_purchase.vehicles.all()
    fleet_vhicles.Update( is_booked = False, is_hired= True )
    transaction = models.Transaction( profile        = request.user.profile,
                                      fleet           = fleet_to_purchase,
                                      amount          = fleet_to_purchase.get_total(),
                                      is_purchased    = True )
    transaction.save()
    messages.info(request, 'Your payment has been done successfully')
    return HttpResponseRedirect(fleet_to_purchase.get_absolute_url())
