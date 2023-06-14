# Generated by Django 4.2.2 on 2023-06-14 06:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0002_alter_household_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='location',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]