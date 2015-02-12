from django.shortcuts import render
from django.views.generic import ListView
from machines.models import Rack

class RackList(ListView):
    model = Rack
    