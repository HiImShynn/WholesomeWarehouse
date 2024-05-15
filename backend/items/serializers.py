"""DS"""
from rest_framework import serializers
from .models import Items, Orders

class OrderSerializer(serializers.ModelSerializer):
    """DS"""
    partner = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        """DS"""
        model = Orders
        fields = [
            'id',
            'partner',
            'order_date',
            'order_status',
        ]

class ItemSerializer(serializers.ModelSerializer):
    """DS"""
    orders = OrderSerializer(read_only = True)
    class Meta:
        """DS"""
        model = Items
        fields = [
            'id',
            'name',
            'description',
            'unit_price',
            'unit_of_measure',
            'current_stock',
            'is_available',
        ]
