# Generated by Django 5.1.2 on 2024-11-27 10:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_remove_floor_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.apartment')),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_staff': False}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]