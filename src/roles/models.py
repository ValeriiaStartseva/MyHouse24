from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=20)


class Permission(models.Model):
    name = models.CharField(max_length=20)


class RolesPermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
