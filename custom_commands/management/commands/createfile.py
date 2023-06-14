from django.core.management.base import BaseCommand, CommandError
from enrolment.models import *
from office.models import Office
from household.models import *
import random
import csv
from random import randint
import datetime
import os


class Command(BaseCommand):
    help = "Creates csv file"

    def handle(self, *args, **kwargs):
        path = os.path.join(os.getcwd(), "enrolment.csv")

        with open(path, "w") as out_file:
            print(f"Preparing to write file: {path}")
            writer = csv.writer(out_file, delimiter=",")

            writer.writerow(
                [
                    "Enrolment ID",
                    "Household ID",
                    "Household",
                    "Recipient",
                    "Cash Offer",
                    "Phone Number",
                ]
            )

            enrolments = Enrolment.objects.all()

            for enrolment in enrolments:
                recipient = Person.objects.filter(household=enrolment.household, is_recipient=True).first()

                row = [
                    enrolment.id,
                    enrolment.household.id,
                    enrolment.household.name,
                    recipient,
                    enrolment.cash_offer,
                    recipient.phone_number,
                ]

                writer.writerow(row)