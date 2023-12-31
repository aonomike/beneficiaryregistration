# Generated by Django 4.2.2 on 2023-06-14 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0003_office_slug_office_uuid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('household', '0003_household_uuid_location_uuid_person_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistanceProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(help_text='Name of Assistance Project', max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_project_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistance_project_modified_by', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.office')),
            ],
            options={
                'verbose_name': 'Assistance project',
                'verbose_name_plural': 'Assistance projects',
            },
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('cash_offer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assistance_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrolment.assistanceproject')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolment_created_by', to=settings.AUTH_USER_MODEL)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolment', to='household.household')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolment_last_modified_by', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.office')),
            ],
            options={
                'verbose_name': 'Enrolment',
                'verbose_name_plural': 'Enrolments',
            },
        ),
    ]
