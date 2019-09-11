from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from . import models, forms

class Vehicles_template_view(generic.TemplateView):
    template_name = 'vehicle/index.html'


class VehicleListView(generic.ListView):
    model = models.Vehicle
    template_name = 'vehicle/vehicle_list.html'
    queryset = models.Vehicle.objects.filter(is_freezed = False, is_approved = True)
    context_object_name = 'CarsList'



class VehicleDetaileView(generic.DetailView):
    model = models.Vehicle
    context_object_name = 'car'

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Vehicle, id = _id)


class VehicleRegisterView(generic.CreateView):
    template_name = 'vehicle/vehicle_form.html'
    form_class = forms.vehicle_reg_form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(VehicleRegisterView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = 'Register'
        return context



class VehicleUpdateView(generic.UpdateView):
    template_name = 'vehicle/vehicle_form.html'
    form_class = forms.vehicle_reg_form
    
    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Vehicle, id = _id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = 'Update'
        return context



class VehicleDeleteView(generic.DeleteView):
    model = models.Vehicle
    success_url = reverse_lazy('vehicle:vehicle_list')


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
