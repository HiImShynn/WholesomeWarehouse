"""DS"""
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from .models import CustomUser

class StaffPermission(BasePermission):
    """DS"""

    def has_permission(self, request, view):
        """DS"""
        user = request.user
        if not user.is_authenticated:
            raise exceptions.AuthenticationFailed('Authentication credentials were not provided!')
        try:
            role = request.user.role
        except KeyError as exc:
            raise exceptions.PermissionDenied('Role not found!') from exc
        if role == CustomUser.Role.STAFF:
            return True
        return False
