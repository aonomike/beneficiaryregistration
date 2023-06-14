import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from office.models import Office
from household.models import Household


class AssistanceProject(models.Model):
    """An Assistance Project is an assistance given to members of a Household"""

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Name of Assistance Project")
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistance_project_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistance_project_modified_by')

    class Meta:
        verbose_name = "Assistance project"
        verbose_name_plural = "Assistance projects"

    def __str__(self):
        return self.name


class Enrolment(models.Model):
    """An Enrolment links a Household to an Assistance project"""

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    assistance_project = models.ForeignKey(AssistanceProject, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, related_name="enrolment", on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    cash_offer = models.DecimalField(max_digits = 5, decimal_places = 2)
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolment_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolment_last_modified_by')

    class Meta:
        verbose_name = "Enrolment"
        verbose_name_plural = "Enrolments"

    def __str__(self):
        return self.household.name
