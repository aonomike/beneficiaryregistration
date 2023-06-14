from django.urls import path
from .views import OfficeListView

urlpatterns = [
    path('office/', OfficeListView.as_view(), name='office_list'),
]