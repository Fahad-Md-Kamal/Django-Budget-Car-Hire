from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from . import models, forms


class AdminFleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/admin_fleets.html'


class FleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/fleet_list.html'


class FleetDetailView(generic.DetailView):
    model = models.Fleet
    template_name = 'fleets/fleet_detail.html'


class FleetCreateView(generic.CreateView):
    form_class = forms.FleetRegisterForm
    template_name = 'fleets/fleet_form.html'


class FleetUpdateView(generic.UpdateView):
    form_class = forms.FleetRegisterForm
    template_name = 'fleets/fleet_form.html'


class FleetDeleteView(generic.DeleteView):
    model = models.Fleet
