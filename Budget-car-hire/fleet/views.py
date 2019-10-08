from django.shortcuts import (render, get_object_or_404, redirect, reverse)
from django.http import (HttpResponseRedirect, HttpResponse)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from uuid import uuid4
from datetime import datetime, date

from users.models import Profile
from .models import Fleet, Transaction
from vehicle.models import Vehicle

import io
from reportlab.pdfgen import canvas
from django.http import FileResponse

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Logged in Users Fleet List View
@login_required
def fleet_view(request):
    template                    = 'fleet/fleets.html'
    req_user                    = request.user.user_profile
    fleets                      = Fleet.objects.filter(user = req_user)
    context                     = {
        'fleets': fleets,
    }
    return render(request, template, context)


# Admins View of all fleets
@login_required
def admin_fleet_view(request):
    template                    = 'fleet/fleet_admin.html'
    req_user                    = request.user.user_profile
    fleets                      = Fleet.objects.filter()
    context                     = {
        'fleets': fleets,
    }
    return render(request, template, context)


# Certain fleet detail view
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


# Activating existing fleet for modification
@login_required
def existing_fleet(request, pk):
    fleet               = get_object_or_404(Fleet, pk = pk)
    request.session['fleet_id'] = fleet.id
    return redirect('vehicle:vehicle_list')


# Creating new fleet for Vehicle booking
def new_fleet(request):
    fleet = Fleet.objects.create(user = request.user.user_profile, fleet_ref = str(uuid4())[-6:].upper())
    messages.info(request, f'Please !!.. Select vehicle for your Fleet')
    request.session['fleet_id'] = fleet.id
    return redirect('vehicle:vehicle_list')


# Adding vehicle to the fleet
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
        if fleet.is_purchased:
            messages.warning(request, f'Cannot modify this Fleet. Please register new Fleet.')
        elif fleet.vehicles.count() >= 10:
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


# Removing vehicle form the fleet
@login_required
def remove_from_fleet(request, fleet_pk, vehicle_pk):
    car             = get_object_or_404(Vehicle, pk = vehicle_pk)
    fleet           = get_object_or_404(Fleet, pk = fleet_pk)
    if request.user.is_staff or request.user.user_profile == fleet.user:
        car.is_hired = False
        car.is_booked = False
        car.save()
        fleet.vehicles.remove(car)
        messages.info(request, f'{car.reg_no} removed form the Fleet')
    else:
        messages.error(request, 'You cannot perform vehicle remove action on this fleet')

    return HttpResponseRedirect(fleet.get_absolute_url())


# Cancel a fleet
@login_required
def cancel_fleet(request, pk):
    fleet      = get_object_or_404(Fleet, pk=pk)
    if fleet.user == request.user.user_profile or request.user.is_staff:
        fleet_vhicles                       = fleet.vehicles.all()
        fleet_vhicles.update( is_hired=False )
        fleet.delete()
        del request.session['fleet_id']
    else:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())

    return HttpResponseRedirect(reverse('fleet:fleets'))


# Removing a fleet
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



# Approving fleet (Admin)
@login_required
def approve_fleet(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())
    fleet      = get_object_or_404(Fleet, pk=pk)
    fleet_vhicles                       = fleet.vehicles.all()
    fleet_vhicles.update( is_booked = False )
    fleet.approved_on = datetime.now()
    fleet.approve()

    # Send Mail After Fleet Approval
    send_mail('Fleet Approved',
        f'Your fleet {fleet.fleet_ref} has ' +
        f'been approved, Your fleet will be active until {fleet.expiration_date().date()} .',
        'randomfahad@gmail.com', [fleet.user.user.email], fail_silently=False )

    return HttpResponseRedirect(reverse('fleet:admin_fleet_view'))


# Block a Fleet 
@login_required
def freeze_fleet(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You cannot perform this action on this fleet')
        return HttpResponseRedirect(fleet.get_absolute_url())
    fleet      = get_object_or_404(Fleet, pk=pk)
    fleet.is_freezed = not fleet.is_freezed
    fleet.save()
    return HttpResponseRedirect(reverse('fleet:admin_fleet_view'))

# Check-out by paying for Fleet
@login_required
def checkout(request, pk):
    template = 'fleet/payment.html'
    fleet_to_pay                    = get_object_or_404(Fleet, pk = pk)
    total = fleet_to_pay.get_total()

    if fleet_to_pay.check_hired():
        messages.warning (request, 'Already Hired vehicle\'s In the Fleet')
        return HttpResponseRedirect(fleet_to_pay.get_absolute_url())
    elif request.user.user_profile != fleet_to_pay.user:
        messages.warning (request, 'You cannot pay for other people\'s fleet.')
    elif request.method == 'POST':
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount= total,
            currency='usd',
            description='Example charge',
            source=token,
        )
        return redirect(reverse ('fleet:update_record', kwargs = {'pk':fleet_to_pay.pk,'token': token}))

    context = {
        'fleet': fleet_to_pay
    }
    return render(request, template, context)
     

# After successfull payment Store payment information
@login_required
def update_payment_record(request, pk, token):
    fleet_purchased                   = get_object_or_404(Fleet, pk = pk)
    fleet_purchased.is_purchased      = True
    fleet_purchased.booked_date       = datetime.now()
    fleet_vehicles                      = fleet_purchased.vehicles.all()
    fleet_vehicles.update(is_hired = True, is_booked = False)
    fleet_purchased.save()

    transaction = Transaction( profile         = request.user.user_profile,
                            fleet           = fleet_purchased,
                            amount          = fleet_purchased.get_total(),
                            token           = token )
    transaction.save()

    # On successful payment send mail to the user
    send_mail('Payment Success',
            f'Payment for fleet {fleet_purchased.fleet_ref} has ' +
            f'been successfully received, Payement confirmation token {token}.',
            'randomfahad@gmail.com', [fleet_purchased.user.user.email], fail_silently=False )

    # Success message.
    messages.success(request, 'Your payment has been done successfully')
    # Redirecting to the fleet
    return HttpResponseRedirect(fleet_purchased.get_absolute_url())



# Generate Fleet Invoice Only after it is paid
def report_generator(request, pk):

    fleet           = get_object_or_404(Fleet, pk= pk)
    payments        = Transaction.objects.filter(fleet=fleet)
    vehicles        = fleet.vehicles.all()

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)

    # Center Text
    p.setFont('Helvetica', 18, leading=None )
    p.drawString(240, 790, 'Budget Car Hire' )
    p.drawString(240, 540, 'Vehicle(s) Detail' )
    p.setFont('Helvetica', 12, leading=None )
    p.drawString(250, 765, 'Fleet Detail Report' )
    # Left Side Information
    p.drawString(30, 730, f'Customer Name : {fleet.user.user.username}' )
    p.drawString(30, 710, f'Booked On : {fleet.booked_date.date()}' )
    p.drawString(30, 690, f'Total Rent : {fleet.get_total()}/-')
    # pos = 670
    # for payment in payments:
    #     p.drawString(30, pos, f'Paid On : {payment.timestamp.date()}')
    #     pos -=30
    # Right Side Information
    p.drawRightString(550, 730,  f'{fleet.fleet_ref} : Reference ID' )
    if fleet.is_approved:
        p.drawRightString(550, 710,  f'{fleet.approved_on.date()} : Start Date' )
        p.drawRightString(550, 690,  f'{fleet.expiration_date().date()} : Expires On' )
    else:
        p.drawRightString(550, 710,  f'Not-Approved Yet' )
    # pos = 670
    # for payment in payments:
    #     p.drawRightString(550, pos,  f'{payment.token} : Token' )
    #     pos -= 30
    for i in range(10,580):
        p.drawString(i, 755, '. .')
    for i in range(10,580):
        p.drawString(i, 650, '. .')
    # Vehicle Details
    p.drawString(30, 500, 'Model')
    p.drawString(150, 500, 'Reg. No.')
    p.drawString(250, 500, 'Capacity')
    p.drawString(350, 500, 'Rent/ Month')
    p.drawString(490, 500, 'Vehicle Type')
    for i in range(10,580):
        p.drawString(i, 485, '. .')
    y = 460
    for car in vehicles:
        p.drawString(30, y, car.get_model_name_display())
        p.drawString(150, y, car.reg_no)
        p.drawString(270, y, str(car.capacity))
        p.drawString(360, y, str(car.rent))
        p.drawString(500, y, car.get_vehicle_type_display())
        y -= 20
    for i in range(30,540):
        p.drawString(i, 255, '. .')

    for i in range(330,540):
        p.drawString(i, 70, '. .')

    # Bottom Left Corner
    pos = 240
    for payment in payments:
        p.drawString(30, pos, f'Paid on:: {payment.timestamp.date()}               Payment Token::     {payment.token}')
        pos -= 20



    # Bottom Right Corner
    p.drawString(400, 120, 'Authorized by:')
    p.drawString(400, 50, 'Budget Car Hire')
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'Fleet-{fleet.fleet_ref}-invoice.pdf')


