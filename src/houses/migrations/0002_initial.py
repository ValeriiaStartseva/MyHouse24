# Generated by Django 5.1.2 on 2024-11-03 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('houses', '0001_initial'),
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartment',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.tariff'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.floor'),
        ),
        migrations.AddField(
            model_name='house',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.gallery'),
        ),
        migrations.AddField(
            model_name='house',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='floor',
            name='house',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='house',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
        ),
        migrations.AddField(
            model_name='section',
            name='house',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
        ),
        migrations.AddField(
            model_name='floor',
            name='section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.section'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.section'),
        ),
    ]
