from django.urls import path
from .views import HouseholdListView, PersonListView, LocationListView

urlpatterns = [
    path('households/', HouseholdListView.as_view(), name='household_list'),
    path('persons/', PersonListView.as_view(), name='persons_list'),
    path('locations/', LocationListView.as_view(), name='locations_list'),
]
