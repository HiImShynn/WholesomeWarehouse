"""DS"""
from django.db import models
from user.models import Partner


class Orders(models.Model):
    """DS"""

    class Status(models.TextChoices):
        """Custom Status"""
        PENDING = "PENDING", "pending"
        DELIVER = "DELIVER", "deliver"
        SHIPPED = "SHIPPED", "shipped"

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null= False)
    order_date = models.DateTimeField(auto_now=True)
    oder_status = models.CharField(max_length=50, choices=Status.choices)

# class Deliveries(models.Model):
#     """DS"""
#     delivery_address = models.CharField(max_length=200, null=False, blank=False)

class Items(models.Model):
    """DS"""

    name = models.CharField(max_length=100, null= False, blank= False)
    description = models.TextField(max_length= 500)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    unit_of_measure = models.CharField(max_length=50)
    current_stock = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=False)
    orders = models.ManyToManyField(Orders)
