# Generated by Django 5.1.2 on 2024-11-27 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
        ('houses', '0009_remove_apartmentowner_apartment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
        ),
    ]
