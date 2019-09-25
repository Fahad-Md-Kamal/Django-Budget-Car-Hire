from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from uuid import uuid4
from datetime import datetime

from users.models import Profile
from .models import Fleet
from vehicle.models import Vehicle

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
def fleet_detail_view(request, pk):
    template            = 'fleet/fleet_detail.html'
    fleet               = get_object_or_404(Fleet, pk = pk)
    fleet_id            = request.session.get('fleet_id', None)
    if fleet_id:
        del request.session['fleet_id']
    context             = {
        'fleet': fleet,
        'vehicles' : fleet.get_fleet_vehicles(),
        'total': fleet.get_total(),
        'msg': request.session.get('fleet_id', None)
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
        elif fleet.vehicles.count == 21:
            messages.info(request, f'You have reached the max number vehicle for a fleet')
        else:
            fleet.vehicles.add(car)
            car.booked(car)
            messages.info(request, f'{car.reg_no} added to fleet {fleet.fleet_ref}')
    
    return HttpResponseRedirect(fleet.get_absolute_url())





# def fleet_home(requset):
#     fleet_id                    = requset.session.get('fleet_id', None)
#     qs                          = Fleet.objects.filter(id=fleet_id)
#     if qs.count()               == 1:
#         fleet_obj               = qs.first()
#     else:
#         fleet_obj               = Fleet.objects.new(customer=requset.user)
#         requset.session['fleet_id'] = fleet_obj.id
#     return render(requset, 'fleet/fleets.html', {})



# def fleet_home(request):
#     fleet_obj, new_obj      = Fleet.objects.new_or_get(request)
#     cars                    = fleet_obj.vehicles.all()
#     total                   = 0
#     for x in cars:
#         total += x.rent
#     print(total)
#     fleet_obj.total         = total
#     fleet_obj.save()
#     return render(request, 'fleet/fleets.html', {})


# def fleet_update(request):
#     car_obj                     = Vehicle.objects.get(id=1)
#     fleet_obj, new_obj          = Fleet.objects.new_or_get(request)
#     fleet_obj.vehicles.add(car_obj)
#     return redirect(car_obj.get_absolute_url())





# @login_required
# def add_to_fleet(request, pk):
#     user                        = request.user.user_profile
#     fleet_id                    = request.COOKIES.get('fleet', None)
#     car                         = get_object_or_404(Vehicle, pk = pk)
#     fleet                       = ''
#     if fleet_id is None:
#         fleet = Fleet.objects.create(user = user, fleet_ref = str(uuid4())[-6:].upper())
#         fleet.vehicles.add(car)
#         car.booked(car)
#         messages.info(request, f'{car.reg_no} added to fleet {fleet.fleet_ref}')
#         response.set_cookie('fleet', 'some_cookie')
#     else:
#         fleet                   = get_object_or_404(Fleet, pk = fleet_id)
#         if not fleet.user == user:
#             messages.error(request, f'You cannot modify this Fleet')
#         else:
#             fleet.vehicles.add(car)
#             messages.info(request, f'{car.reg_no} added to fleet {fleet.fleet_ref}')
#     return HttpResponseRedirect(fleet.get_absolute_url())