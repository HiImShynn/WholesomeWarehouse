"""DS"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Orders  # Import the correct model
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    """DS"""
    permission_classes = [IsAuthenticated]
    queryset = Orders.objects.all()  # Use the correct model
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(partner=self.request.user.id)
        return super().perform_create(serializer)
