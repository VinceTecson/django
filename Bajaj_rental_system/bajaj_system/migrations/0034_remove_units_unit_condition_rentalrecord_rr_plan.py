# Generated by Django 5.0.3 on 2024-05-20 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0033_remove_units_unit_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalrecord',
            name='rr_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bajaj_system.rental_plans'),
        ),
    ]
