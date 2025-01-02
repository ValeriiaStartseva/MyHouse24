# Generated by Django 5.1.2 on 2024-11-27 11:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0008_apartmentowner'),
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('apartment_area', models.FloatField(default=0.0)),
                ('floor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.floor')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.section')),
                ('tariff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.tariff')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.apartment')),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_staff': False}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
