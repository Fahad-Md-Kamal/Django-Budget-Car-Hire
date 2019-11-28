# Deleveoped By
# Fahad Md Kamal
# NCC ID: 00171328

#pylint: disable = no-member, unused-variable, undefined-variable
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.mail import send_mail

from datetime import date, datetime


import re

from . import models, forms
from fleet.models import Fleet


def vehicle_list_view(request):
    template        = 'vehicle/vehicle_list.html'
    fleet_id        = request.session.get('fleet_id', None)
    fleet_cars      = ''
    if fleet_id:
        fleet       = get_object_or_404(Fleet, pk=fleet_id)
        fleet_cars  = fleet.get_fleet_vehicles()

    CarsList        = models.Vehicle.objects.filter(is_freezed = False, 
                                is_approved = True, 
                                is_hired = False)

    page = request.GET.get('page', 1)
    paginator = Paginator(CarsList, 5)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'cars'          : cars,
        'page_heading'  : 'Available',
        'vehicle_list'  : models.Vehicle.objects.all(),
        'fleet_cars'    : fleet_cars,
        'form'          : forms.vehicle_model_form()
    }
    return render(request, template, context)


def vehicle_detail_view(request, pk):
    template        = 'vehicle/vehicle_detail.html'
    context = {
        'car':get_object_or_404(models.Vehicle, pk=pk)
    }
    return render(request, template, context)


@login_required
def vehicle_registration(request):
    template        = 'vehicle/vehicle_form.html'
    if request.method == 'POST':
        form = forms.vehicle_reg_form(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            model_date = form.cleaned_data['model_year']
            # Check The Date
            if (model_date - datetime.now().date()).days > 0:
                messages.warning(request, "Invalid Date")
            else:
                vehicle.owner = request.user
                vehicle = form.save()
                messages.success(request, f'Vehicle {vehicle.reg_no} registared successfully. We will notify you when approved')
                return HttpResponseRedirect(vehicle.get_absolute_url())
    else:
        form = forms.vehicle_reg_form()
    context = {
        'form': form,
        'state': 'Register'
    }
    return render(request, template, context)


@login_required
def vehicle_update_view(request, pk):
    template        = 'vehicle/vehicle_form.html'
    vehicle         = get_object_or_404(models.Vehicle, id = pk)
    user            = request.user
    if user.is_staff or user == vehicle.owner:
        if request.method == 'POST':
            form     = forms.vehicle_reg_form(request.POST, instance = vehicle)
            if form.is_valid():
                vehcile = form.save( commit= False)
                model_date = form.cleaned_data['model_year']
                # Check The Date
                if (model_date - datetime.now().date()).days > 0:
                    messages.warning(request, "Invalid Date")
                else:
                    vehcile.is_approved = False
                    vehcile.save()
                    messages.info(request, f'Vehicle {vehicle.reg_no} updated successfully')
                    return HttpResponseRedirect(vehicle.get_absolute_url())
            else:
                messages.error(request, 'Failed to update vehicle')
        else:
            form = forms.vehicle_reg_form(instance=vehicle)
        context = {
            'form':form,
            'state': 'Update'
        }
        return render(request, template, context)
    else:
        messages.error(request, 'You have no permission to update this vehicle')
        return HttpResponseRedirect(vehicle.get_absolute_url())


@login_required
def vehicel_delete_view(request, pk):
    template        = 'vehicle/vehicle_confirm_delete.html'
    car             = get_object_or_404(models.Vehicle, id = pk)
    user            = request.user
    if user.is_staff or car.owner == user:
        if request.method == 'POST':
            car.delete()
            messages.info(request, 'Vehicle deleted successfully')
            return redirect ('vehicle:vehicle_list')
        else:
            messages.error(request, 'Failed to delete the vehicle')
            context = {
                'car':car
            }
            return render(request, template, context)
    else:
        messages.error(request, 'You have no permission')
        return HttpResponseRedirect(car.get_absolute_url())   


def admin_vehicle_view(request):
    template    = 'vehicle/vehicle_admin.html'
    cars_list   = models.Vehicle.objects.all()
    context = {
        'cars_list': cars_list
    }
    return render(request, template, context)


def approve_vehicle(request, pk):
    vehicle = get_object_or_404(models.Vehicle, pk =pk)
    vehicle.approve_vehicle()
    
    send_mail('Vehicle Approved',
        f'Your vehicle {vehicle.reg_no} has been approved.',
        'randomfahad@gmail.com', [vehicle.owner.email], fail_silently=False )
    return redirect('vehicle:admin_vehicle')


def freeze_vehicle(request, pk):
    vehicle = get_object_or_404(models.Vehicle, pk =pk)
    vehicle.freeze_vehicle()
    return redirect('vehicle:admin_vehicle')


def owner_vehicle_list(request):
    template        = 'vehicle/vehicle_list.html'
    CarsList        = models.Vehicle.objects.filter(owner = request.user)
    context = {
        'cars': CarsList,
        'page_heading' : request.user.username + '\'s',
        'form'          : forms.vehicle_model_form()
    }
    return render (request, template, context)


def search_vehicle(request):
    template        = 'vehicle/vehicle_list.html'
    vehicle_list        = models.Vehicle.objects.filter(is_approved = True)

    vehicel_type    = request.GET.get('vehicel_type', None)
    model_name   = request.GET.get('model_name', None)
    query_text      = request.GET.get('query_text', None)

    if query_text != '' and query_text is not None:
        CarsList = vehicle_list.filter(reg_no__icontains=query_text)

    elif vehicel_type != '' and vehicel_type is not None:
        CarsList = vehicle_list.filter(vehicle_type=vehicel_type)

    elif model_name != '':
        try:
            CarsList = vehicle_list.filter(model_name=model_name)
        except:
            CarsList = None

    context = {
        'cars':CarsList,
        'page_heading' : 'Filtered',
        'form' : forms.vehicle_model_form()
    }
    return render (request, template, context)    
