from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Office(models.Model):
    """Country Office Model"""

    iso_code = models.CharField(max_length=5, blank=False, null = False)
    name = models.CharField(max_length=100, help_text='Country Office', null = False)
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='office_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='office_last_modified_by')

    class Meta:
        unique_together = ("iso_code", "name")
        verbose_name = "Office"

    def __str__(self):
        return self.name
