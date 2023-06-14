from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from office.models import Office

class Location(models.Model):
    """
    Location object represents a geographical location
    """
    name = models.CharField(max_length=200, help_text="Name")
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='location_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='location_last_modified_by')
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name
    
class Household(models.Model):
    """Household Model"""

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="Household Name")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='household_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='household_last_modified_by')

    class Meta:
        verbose_name = "Household"
        verbose_name_plural = "Households"

    def __str__(self):
        return self.name


class Person(models.Model):
    """Person Model"""

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, help_text="First Name")
    last_name = models.CharField(max_length=200, help_text="Last Name")
    phone_number = models.CharField(max_length=255,blank=False, help_text="Phone Number")
    is_recipient = models.BooleanField()
    creation_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person_created_by')
    last_modified_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person_last_modified_by')
    

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

