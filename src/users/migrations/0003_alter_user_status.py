# Generated by Django 5.1.2 on 2024-11-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('new', 'Новий'), ('active', 'Активний'), ('disabled', 'Неактивний')], default='new', max_length=20),
        ),
    ]