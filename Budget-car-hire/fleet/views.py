from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from uuid import uuid4
from datetime import datetime, date

from users.models import Profile
from .models import Fleet, Transaction
from vehicle.models import Vehicle

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

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
def admin_fleet_view(request):
    template                    = 'fleet/fleet_admin.html'
    req_user                    = request.user.user_profile
    fleets                      = Fleet.objects.filter()
    context                     = {
        'fleets': fleets,
    }
    return render(request, template, context)



@login_required
def fleet_detail_view(request, pk, car_pk=None):
    template            = 'fleet/fleet_detail.html'
    fleet               = get_object_or_404(Fleet, pk = pk)
    request.session['fleet_id'] = fleet.id
    car                 = ''
    if car_pk:
        car                 = get_object_or_404(Vehicle, pk = car_pk)
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

def new_fleet(request):
    fleet = Fleet.objects.create(user = request.user.user_profile, fleet_ref = str(uuid4())[-6:].upper())
    messages.info(request, f'Select vehicle for your Fleet')
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
        if fleet.vehicles.count() >= 10:
            messages.warning(request, f'You have reached the limit of 10')
        elif not fleet.user == user:
            messages.success(request, f'You cannot modify this Fleet')
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
        messages.info(request, f'{car.reg_no} removed form the Fleet')
    else:
        messages.error(request, 'You cannot perform vehicle remove action on this fleet')

    return HttpResponseRedirect(fleet.get_absolute_url())


@login_required
def cancel_fleet(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())

    fleet      = get_object_or_404(Fleet, pk=pk)
    fleet.delete()
    del request.session['fleet_id']
    
    return HttpResponseRedirect(reverse('fleet:fleets'))



@login_required
def remove_fleet(request, pk):
    fleet           = get_object_or_404(Fleet, pk = pk)
    if request.user.user_profile == fleet.user:
        Fleet.delete(fleet)
        messages.info(request, f'{fleet.fleet_ref} removed')
        del request.session['fleet_id']
    else:
        fleet.delete()
        messages.error(request, 'You cannot perform this action on this fleet')

    if request.user.is_staff:
        return HttpResponseRedirect(reverse('fleet:admin_fleet_view'))
    else:
        return redirect ('fleet:fleets')


@login_required
def approve_fleet(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())
    fleet      = get_object_or_404(Fleet, pk=pk)
    fleet_vhicles                       = fleet.vehicles.all()
    fleet_vhicles.update( is_hired= True )
    fleet.approved_on = datetime.now()
    fleet.approve()
    return HttpResponseRedirect(reverse('fleet:admin_fleet_view'))


@login_required
def freeze_fleet(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())
    fleet      = get_object_or_404(Fleet, pk=pk)
    fleet.is_freezed = not fleet.is_freezed
    fleet.save()
    return HttpResponseRedirect(reverse('fleet:admin_fleet_view'))

    
@login_required
def checkout(request, pk):
    template = 'fleet/payment.html'
    fleet_to_pay                    = get_object_or_404(Fleet, pk = pk)
    total = fleet_to_pay.get_total()
    if request.method == 'POST':
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount= total,
            currency='usd',
            description='Example charge',
            source=token,
        )
        return redirect(reverse ('fleet:update_record', kwargs = {'pk':fleet_to_pay.pk,'token': token}))

    context = {
        'total': total
    }
    return render(request, template, context)
     

@login_required
def update_payment_record(request, pk, token):
    fleet_to_purchase                   = get_object_or_404(Fleet, pk = pk)
    fleet_to_purchase.is_purchased      = True
    fleet_to_purchase.booked_date       = datetime.now()
    fleet_to_purchase.save()

    transaction = Transaction( profile         = request.user.user_profile,
                                      fleet           = fleet_to_purchase,
                                      amount          = fleet_to_purchase.get_total(),
                                      token           = token )
    transaction.save()
    # Success message.
    messages.success(request, 'Your payment has been done successfully')
    # Redirecting to the fleet
    return HttpResponseRedirect(fleet_to_purchase.get_absolute_url())
