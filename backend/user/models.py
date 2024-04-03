""" Docstring for models.py """
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save()

class StaffManager(BaseUserManager):
    """Staff manager"""
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STAFF)
    
class PartnerManager(BaseUserManager):
    """Partner manager"""
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.PARTNER)

class Staff(CustomUser):
    """
    Staff model
    """
    base_role = CustomUser.Role.STAFF
    class Meta:
        """Docstring"""
        proxy = True

class Partner(CustomUser):
    """
    Partner model
    """
    base_role = CustomUser.Role.PARTNER
    class Meta:
        """Docstring"""
        proxy = True
