from django.shortcuts import render, get_object_or_404

from users.models import Profile
from .models import Fleet
from vehicle.models import Vehicle

# def get_user_pending_fleet(request):
#     user_profile    = get_object_or_404(Profile, user=request.user)
#     fleet           = Fleet.objects.filter(customer= user_profile, is_hired= False)
#     if fleet.exists():
#         return fleet[0]
#     return 0


# def add_to_fleet(request, **kwargs):
#     # get the user profile
#     user_profile    = get_object_or_404(Profile, user=request.user)
#     # filter vehicle id
#     vehicle         = Vehicle.objects.filter(id=kwargs.get('vehicle_id', "")).first()
#     # Check if the user already owns this vehicle
#     if vehicle in 

def fleet_create(customer=None):
    fleet_obj       = Fleet.objects.create(customer=None)
    print('Fleet Id Created')
    return fleet_obj




def fleet_home(requset):
    # del requset.session['fleet_id']
    requset.session['fleet_id'] = "12"
    fleet_id = requset.session.get('fleet_id', None)
    # if fleet_id is None:
    #     fleet_obj   = fleet_obj()
    #     requset.session['fleet_id'] = fleet_obj.id
    # else:
    qs = Fleet.objects.filter(id=fleet_id)
    if qs.count() == 1:
        fleet_obj   = qs.first()
    else:
        fleet_obj   = fleet_create()
        requset.session['fleet_id'] = fleet_obj.id

    return render(requset, 'fleet/fleets.html', {})