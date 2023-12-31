# Generated by Django 4.2.2 on 2023-06-14 03:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=5)),
                ('name', models.CharField(help_text='Country Office', max_length=100)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2023, 6, 14, 3, 6, 16, 579898, tzinfo=datetime.timezone.utc))),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime(2023, 6, 14, 3, 6, 16, 579923, tzinfo=datetime.timezone.utc))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Office',
                'unique_together': {('iso_code', 'name')},
            },
        ),
    ]
