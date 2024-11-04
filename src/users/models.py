from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin
from django.db import models
from src.core.models import GalleryImage


class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = (
        ("new", "новий"),
        ("active", "активний"),
        ("disabled", "неактивний"),
    )

    name = models.CharField(max_length=50, blank=True)
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

    role = models.ManyToManyField(Group, blank=True, related_name="custom_user_set")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_permission(self, perm_codename):
        """
        Check if user has a specific permission
        """
        return self.role.permissions.filter(codename=perm_codename).exists()

    def has_role(self, role_name):
        """
        Check if user has a specific role
        """
        return self.role.filter(name=role_name).exists()
