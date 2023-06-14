from django.urls import path
from .views import HouseholdListView, PersonListView

urlpatterns = [
    path('households/', HouseholdListView.as_view(), name='household_list'),
    path('persons/', PersonListView.as_view(), name='persons_list'),
]
