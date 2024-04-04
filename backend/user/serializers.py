"""DOCSTRING"""
from rest_framework import serializers
from .models import Staff, Partner

class StaffSerializer(serializers.ModelSerializer):
    """DOCSTRING"""
    role = serializers.CharField(read_only=True)
    class Meta:
        """DOCSTRING"""
        model = Staff
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
        ]

class PartnerSerializer(serializers.ModelSerializer):
    """DOCSTRING"""
    role = serializers.CharField(read_only=True)
    class Meta:
        """DOCSTRING"""
        model = Partner
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
        ]
