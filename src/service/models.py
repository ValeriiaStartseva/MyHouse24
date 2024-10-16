from django.db import models


class UnitOfChange(models.Model):
    name = models.CharField(max_length=30)


class Service(models.Model):
    name = models.CharField(max_length=30)
    unit_of_change = models.ForeignKey(UnitOfChange, on_delete=models.CASCADE)
    show_in_meters = models.BooleanField()


class Tariff(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class ServicePrice(models.Model):
    price = models.FloatField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
