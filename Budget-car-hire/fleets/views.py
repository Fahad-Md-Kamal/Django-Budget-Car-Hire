from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from . import models, forms


class AdminFleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/admin_fleets.html'


class FleetListView(generic.ListView):
    model = models.Fleet
    template_name = 'fleets/fleet_list.html'
    context_object_name = 'fleets_list'

    def get_queryset(self):
        return models.Fleet.objects.filter(owner = self.request.user)


class FleetDetailView(generic.DetailView):
    model = models.Fleet
    template_name = 'fleets/fleet_detail.html'
    context_object_name = 'fleet'

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Fleet, id = _id)


class FleetCreateView(generic.CreateView):
    form_class = forms.FleetRegisterForm
    template_name = 'fleets/fleet_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super( FleetCreateView, self ).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
