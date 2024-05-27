"""DOCSTRING"""
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
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

class RegisterStaffSerializer(serializers.ModelSerializer):
    """DOSCTRING"""
    password = serializers.CharField(
        write_only = True, required = True, validators = [validate_password]
    )
    password2 = serializers.CharField(write_only = True, required = True)
    class Meta:
        """DOCSTRING"""
        model = Staff
        fields = [
            'email',
            'username',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if not attrs['email']:
            raise serializers.ValidationError(
                {
                    "email": "Email was not provided."
                }
            )
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    "password": "Password fields do not match."
                }
            )
        return attrs

    def create(self, validated_data):
        """DS"""
        password = validated_data.pop('password', None)
        validated_data.pop('password2', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RegisterPartnerSerializer(serializers.ModelSerializer):
    """DOSCTRING"""
    password = serializers.CharField(
        write_only = True, required = True, validators = [validate_password]
    )
    password2 = serializers.CharField(write_only = True, required = True)
    class Meta:
        """DOCSTRING"""
        model = Partner
        fields = [
            'email',
            'username',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if not attrs['email']:
            raise serializers.ValidationError(
                {
                    "email": "Email was not provided."
                }
            )
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    "password": "Password fields do not match."
                }
            )
        return attrs

    def create(self, validated_data):
        """DS"""
        password = validated_data.pop('password', None)
        validated_data.pop('password2', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
