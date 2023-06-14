from django.urls import path
from .views import EnrolmentListView, PersonListView, AssistancePrijectListView

urlpatterns = [
    path('assistance_projects/', AssistancePrijectListView.as_view(), name='assistance_projects_list'),
    path('enrollments/', EnrolmentListView.as_view(), name='enrolment_list'),
]
