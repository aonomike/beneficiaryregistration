from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from enrolment.models import *
from office.models import *
from household.models import *
import random


from random import randint
import datetime


class Command(BaseCommand):
    help = 'Creates Households'
    
    

    def handle(self, *args, **kwargs):
        fake = Faker()

        
        office = Office.objects.all().first()
        user = User.objects.all().first()
        
        
        for index in range(10):
            location = Location.objects.create(name=fake.company(), created_by=user, last_modified_by=user)
            self.stdout.write(f"Creating Household {index}")
            household = Household.objects.create(office=office, name=fake.name(), created_by=user, last_modified_by=user, location=location)

            for i in range(5):
                self.stdout.write(f"\t Creating member {i}")
                
                Person.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), household=household, created_by=user, last_modified_by=user, phone_number=fake.phone_number(), is_recipient=0)
        
