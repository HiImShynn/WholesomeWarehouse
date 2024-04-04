""" Docstring for models.py """
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom User class to differentiate between Staff and Franchise Partner
    """
    class Role(models.TextChoices):
        """
        Custom Role enums to choose from
        """
        STAFF = "STAFF", 'Staff'
        PARTNER = "PARTNER", 'Partner'

    base_role = Role.STAFF

    role = models.CharField(max_length=50, choices=Role.choices)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save()

class StaffManager(models.Manager):
    """Staff manager"""
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        """Docstring"""
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STAFF)

class PartnerManager(models.Manager):
    """Partner manager"""
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        """Docstring"""
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.PARTNER)

class Staff(CustomUser):
    """
    Staff model
    """
    base_role = CustomUser.Role.STAFF
    objects = StaffManager()
    class Meta:
        """Docstring"""
        proxy = True

class Partner(CustomUser):
    """
    Partner model
    """
    base_role = CustomUser.Role.PARTNER
    objects = PartnerManager()
    class Meta:
        """Docstring"""
        proxy = True
