"""DS"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Orders, Items  # Import the correct model
from .serializers import OrderSerializer, ItemSerializer
from user.permissions import StaffPermission

class OrderViewSet(ModelViewSet):
    """DS"""
    permission_classes = [IsAuthenticated]
    queryset = Orders.objects.all()  # Use the correct model
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(partner=self.request.user.id)
        return super().perform_create(serializer)

class ItemViewSet(ModelViewSet):
    """DS"""
    permission_classes = [IsAuthenticated, StaffPermission]
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
