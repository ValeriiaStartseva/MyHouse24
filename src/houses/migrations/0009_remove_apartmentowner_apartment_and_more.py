# Generated by Django 5.1.2 on 2024-11-27 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0008_apartmentowner'),
        ('payments_section', '0003_alter_personalaccount_apartment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentowner',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartmentowner',
            name='user',
        ),
        migrations.DeleteModel(
            name='Apartment',
        ),
        migrations.DeleteModel(
            name='ApartmentOwner',
        ),
    ]
