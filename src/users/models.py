from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from src.core.models import GalleryImage


class User(AbstractBaseUser):
    STATUS_CHOICES = (
        ("new", "новий"),
        ("active", "активний"),
        ("disabled", "неактивний"),
    )

    name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    third_name = models.CharField(max_length=20, null=True, blank=True)
    birthday_date = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    viber = models.CharField(max_length=20, null=True, blank=True, unique=True)
    telegram = models.CharField(max_length=20, null=True, blank=True, unique=True)
    user_avatar = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user_avatar",
    )
    about_me = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    role = models.ForeignKey

    class Meta:
        permissions = []
