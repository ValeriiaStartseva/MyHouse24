# Generated by Django 5.1.2 on 2024-12-10 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_unit_of_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('income', 'Приходи'), ('expenses', 'Витрати')], default='income', max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='tariff',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
