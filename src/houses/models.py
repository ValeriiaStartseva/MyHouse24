from django.db import models
from src.core.models import Gallery
from src.users.models import User
from src.service.models import Tariff


class House(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=40)
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, null=True, blank=True
    )
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Section(models.Model):
    name = models.CharField(max_length=20)
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True)


class Floor(models.Model):
    number = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True)


class Apartment(models.Model):
    number = models.IntegerField()
    apartment_area = models.FloatField
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, null=True, blank=True)
