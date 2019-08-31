from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from . import models, forms

class Vehicles_template_view(generic.TemplateView):
    template_name = 'vehicle/index.html'


class VehicleListView(generic.ListView):
    model = models.Vehicle
    template_name = 'vehicle/vehicle_list.html'
    queryset = models.Vehicle.objects.all()


class VehicleDetaileView(generic.DetailView):
    model = models.Vehicle

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(models.Vehicle, id = _id)


class VehicleRegisterView(generic.CreateView):
    template_name = 'vehicle/vehicle_form.html'
    form_class = forms.vehicle_reg_form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VehicleRegisterView, self).form_valid(form)



class VehicleUpdateView(generic.UpdateView):
    template_name = 'vehicle/vehicle_form.html'
    form_class = forms.vehicle_reg_form
    
    def get_object(self):
        # _id = self.kwargs.get("pk")
        return get_object_or_404(models.Vehicle, id = self.request.id)



class VehicleDeleteView(generic.DeleteView):
    model = models.Vehicle
    success_url = reverse_lazy('vehicle:vehicle_list')