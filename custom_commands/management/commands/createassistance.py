from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from enrolment.models import *
from office.models import *
from household.models import *
from enrolment.models import *
import random


class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        fake = Faker()

        
        user = User.objects.all().first()
        office_name = fake.company()
        office = Office.objects.create(name=office_name,created_by=user, last_modified_by=user, iso_code=f"{office_name[:1]}-co")

        for index in range(3):
            office = Office(name=f"Office-{index}", iso_code=f"co-{index}", created_by=user, last_modified_by=user,)
            office.save()

            print(f'Successfully created office {office}')
            for counter in range(5):
                fake = Faker()
                user = User.objects.all().first()
                assistance_project = AssistanceProject.objects.create(office=office,
                                            name=f"Assistance-{counter}-{office.iso_code}",
                                            start_date = fake.date_time(),
                                            end_date=fake.date_time(),
                                            created_by=user, last_modified_by=user,
                                            )
                print(f'Successfully created assistance project: {assistance_project}')
