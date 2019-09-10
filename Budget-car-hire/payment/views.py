from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import forms
from fleets.models import Fleet

class MakePayment(generic.CreateView):
    template_name = 'payment/payment_user.html'
    form_class = forms.FleetPaymentForm
    
    def get_context_data(self, **kwargs):
        context = super(MakePayment, self).get_context_data(**kwargs)
        
        ## Calculates all the vehicles monthly payable rent
        _id = self.kwargs.get("pk")
        context['fleetId'] = _id
        fleet = get_object_or_404(Fleet, id = _id)
        context['total'] = 0
        for car in fleet.fleet_vehicles.all():
            context['total'] += car.rent_per_month
        return context
    
    def post(self, request, *args, **kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            

    # def post(self, *args, **kwargs):
    #     payment = super(MakePayment, self).save(commit=False) 
    #     _id = self.kwargs.get("pk")
    #     fleet = get_object_or_404(Fleet, id = _id)
    #     total = 0
    #     for car in fleet.fleet_vehicles.all():
    #         total += car.rent_per_month
    #     payment.fleet = fleet
    #     payment.paid_amount = total
    #     payment.save()




    