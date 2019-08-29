from django.shortcuts import render
from django.views import generic


class Vehicles_template_view(generic.TemplateView):
    template_name = 'vehicle/index.html'
