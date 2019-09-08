from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy

from vehicle.models import Vehicle
from . import models, forms


class AdminFleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/admin_fleets.html'
    context_object_name = 'fleets_list'


class FleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/fleet_list.html'
    context_object_name = 'fleets_list'

    def get_queryset(self):
        return get_list_or_404(models.Fleet.objects.filter(owner = self.request.user))


class FleetDetailView(generic.DetailView):
    model = models.Fleet
    template_name = 'fleets/fleet_detail.html'
    context_object_name = 'fleet'

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Fleet, id = _id)

    def get_context_data(self, **kwargs):
        context = super(FleetDetailView, self).get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.filter(is_freezed = False, is_approved=True, is_hired = False)
        
        print(context['vehicles'])
        
        _id = self.kwargs.get("pk")
        fleet = get_object_or_404(models.Fleet, id = _id)
        context['total'] = 0
        for car in fleet.fleet_vehicles.all():
            context['total'] += car.rent_per_month
        return context


class FleetCreateView(generic.CreateView):
    form_class = forms.FleetRegisterForm
    template_name = 'fleets/fleet_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super( FleetCreateView, self ).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FleetCreateView, self).get_context_data(**kwargs)
        context['state'] = 'Register'
        return context


class FleetUpdateView(generic.UpdateView):
    form_class = forms.FleetRegisterForm
    template_name = 'fleets/fleet_form.html'

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Fleet, id = _id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = 'Update'
        return context


class FleetDeleteView(generic.DeleteView):
    model = models.Fleet
    success_url = reverse_lazy('fleets:fleet_list')


def fleet_approve(request, pk):
    fleet = get_object_or_404(models.Fleet.objects.filter(pk = pk))
    models.Fleet.approve(fleet)
    return redirect('fleets:fleet_detail', pk = fleet.pk)


def fleet_freeze(request, pk):
    fleet = get_object_or_404(models.Fleet.objects.filter(pk = pk))
    models.Fleet.freezed(fleet)
    return redirect('fleets:admin_fleets')


def add_fleet_car(request, carpk, fleetpk):
    car = get_object_or_404(Vehicle.objects.filter(pk = carpk))
    fleet = get_object_or_404(models.Fleet.objects.filter(pk = fleetpk))
    car.hire_vehicle(car)
    if fleet.is_approved == True:
        fleet.approve(fleet)
    fleet.fleet_vehicles.add(car)
    return redirect('fleets:fleet_detail', pk = fleet.pk)

def remove_fleet_car(request, carpk, fleetpk):
    car = get_object_or_404(Vehicle.objects.filter(pk = carpk))
    fleet = get_object_or_404(models.Fleet.objects.filter(pk = fleetpk))
    car.hire_vehicle(car)
    fleet.fleet_vehicles.remove(car)
    return redirect('fleets:fleet_detail', pk = fleet.pk)