from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import forms
from fleets.models import Fleet

class MakePayment(generic.CreateView):
    template_name = 'payment/payment_user.html'
    form_class = forms.FleetPaymentForm


    def get_context_data(self, **kwargs):
        context = super(MakePayment, self).get_context_data(**kwargs)

        # Calculates all the vehicles monthly payable rent
        _id = self.kwargs.get("pk")
        context['fleetId'] = _id
        fleet = get_object_or_404(Fleet, id = _id)
        context['total'] = Fleet.get_fleet_total(fleet)
        return context
    

    def form_valid(self, form):
        _id = self.kwargs.get("pk")
        fleet = get_object_or_404(Fleet, id = _id)
        form.instance.fleet = fleet
        form.instance.paid_amount = Fleet.get_fleet_total(fleet)
        fleet.paid(fleet)
        return super(MakePayment, self).form_valid(form)

            


    