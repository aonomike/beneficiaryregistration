from django.shortcuts import render
from django.db import models
from .models import Office
from django.views.generic import ListView


class OfficeListView(ListView):
    model = Office
    template_name = 'office/index.html'
    context_object_name = 'offices'
    paginate_by = 1


