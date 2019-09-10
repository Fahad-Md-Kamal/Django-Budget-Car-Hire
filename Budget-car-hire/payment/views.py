from django.shortcuts import render
from django.views import generic


class MakePayment(generic.TemplateView):
    template_name = 'payment/payment_user.html'
    
    def get_context_data(self, **kwargs):
        context = super(MakePayment, self).get_context_data(**kwargs)
        context['msg'] = 'This is payment page'
        return context