#pylint: disable = no-member, unused-variable
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from . import models, forms

class Vehicles_template_view(generic.TemplateView):
    template_name = 'vehicle/index.html'


# class VehicleListView(generic.ListView):
#     model = models.Vehicle
#     template_name = 'vehicle/vehicle_list.html'
#     queryset = models.Vehicle.objects.filter(is_freezed = False, is_approved = True)
#     context_object_name = 'CarsList'



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



# class VehicleDetaileView(generic.DetailView):
#     model = models.Vehicle
#     context_object_name = 'car'

#     def get_object(self):
#         _id = self.kwargs.get("pk")
#         return get_object_or_404(models.Vehicle, id = _id)


def vehicle_detail_view(request, pk):
    template            = 'vehicle/vehicle_detail.html'
    car                 = get_object_or_404(models.Vehicle, pk=pk)
    context = {
        'car':car
    }
    return render(request, template, context)


# class VehicleRegisterView(generic.CreateView):
#     template_name = 'vehicle/vehicle_form.html'
#     form_class = forms.vehicle_reg_form

#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(VehicleRegisterView, self).form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['state'] = 'Register'
#         return context



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
