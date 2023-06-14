from django.shortcuts import render
from django.db import models
from .models import *
from django.views.generic import ListView


class HouseholdListView(ListView):
    model = Household
    template_name = 'household/index.html'
    context_object_name = 'households'
    paginate_by = 20
    
class PersonListView(ListView):
    model = Person
    template_name = 'persons/index.html'
    context_object_name = 'persons'
    paginate_by = 20
    
class LocationListView(ListView):
    model = Location
    template_name = 'locations/index.html'
    context_object_name = 'locations'
    paginate_by = 20