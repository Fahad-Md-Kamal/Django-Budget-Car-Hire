#pylint: disable = no-member, unused-variable
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

from . import models, forms

class Vehicles_template_view(generic.TemplateView):
    template_name = 'vehicle/index.html'


def vehicle_list_view(request):
    template                = 'vehicle/vehicle_list.html'
    CarsList       = models.Vehicle.objects.filter(is_freezed = False, 
                                                            is_approved = True, 
                                                            is_booked = False, 
                                                            is_hired = False)
    context = {
        'CarsList' : CarsList
    }
    return render(request, template, context)


def vehicle_detail_view(request, pk):
    template            = 'vehicle/vehicle_detail.html'
    car                 = get_object_or_404(models.Vehicle, pk=pk)
    context = {
        'car':car
    }
    return render(request, template, context)


@login_required
def vehicle_registration(request):
    template = 'vehicle/vehicle_form.html'
    if request.method == 'POST':
        form = forms.vehicle_reg_form(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)

            vehicle.owner = request.user
            vehicle = form.save()
            messages.success(request, f'Vehicle {vehicle.reg_no} registared successfully.')
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

    if not user.is_staff or not user == vehicle.owner:
        messages.error(request, 'You have no permission to update this vehicle')
        return HttpResponseRedirect(vehicle.get_absolute_url())

    if request.method == 'POST':
        form     = forms.vehicle_reg_form(request.POST, instance = vehicle)
        if form.is_valid():
            form.save()
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


# class VehicleDeleteView(generic.DeleteView):
#     model = models.Vehicle
#     success_url = reverse_lazy('vehicle:vehicle_list')


@login_required
def vehicel_delete_view(request, pk):
    template        = 'vehicle/vehicle_confirm_delete.html'
    car         = get_object_or_404(models.Vehicle, id = pk)
    user            = request.user

    if not user.is_staff or not car.owner == user:
        messages.error(request, 'You have no permission')
        return HttpResponseRedirect(car.get_absolute_url())   

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


class AdminVehicleView(generic.ListView):
    model = models.Vehicle
    template_name = 'vehicle/vehicle_admin.html'
    context_object_name = 'cars_list'


def approve_vehicle(self, pk):
    vehicle = get_object_or_404(models.Vehicle, pk =pk)
    vehicle.approve_vehicle()
    return redirect('vehicle:admin_vehicle')


def freeze_vehicle(self, pk):
    vehicle = get_object_or_404(models.Vehicle, pk =pk)
    vehicle.freeze_vehicle()
    return redirect('vehicle:admin_vehicle')

