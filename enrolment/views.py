from django.shortcuts import render
from django.db import models
from .models import *
from django.views.generic import ListView


class AssistanceProjectListView(ListView):
    model = AssistanceProject
    context_object_name = 'households'
    paginate_by = 20
    
class EnrolmentListView(ListView):
    model = Enrolment
    context_object_name = 'persons'
    paginate_by = 20