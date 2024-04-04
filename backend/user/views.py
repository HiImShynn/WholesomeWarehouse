"""DOCSTRING"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Staff, Partner
from .serializers import StaffSerializer, PartnerSerializer

class ListStaff(APIView):
    """DOCSTRING"""
    def get(self, request):
        list_of_staffs = Staff.objects.all()
        serializer = StaffSerializer(list_of_staffs, many=True)
        return Response(
            {
                'message': 'Success',
                'data': serializer.data,
                'status': status.HTTP_200_OK,
            }, status=status.HTTP_200_OK
        )

class ListPartner(APIView):
    """DOCSTRING"""
    def get(self, request):
        list_of_partners = Partner.objects.all()
        serializer = PartnerSerializer(list_of_partners, many=True)
        return Response(
            {
                'message': 'Success',
                'data': serializer.data,
                'status': status.HTTP_200_OK,
            }, status=status.HTTP_200_OK
        )

# CreateAPIView -> Create Partner
class CreatePartner(CreateAPIView):
    """DOCSTRING"""
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class CreateStaff(CreateAPIView):
    """DOCSTRING"""
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class RetrieveUpdateDeletePartner(RetrieveUpdateDestroyAPIView):
    """DOCSTRING"""
    # Set permission to request.user == objects.user
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class RetrieveUpdateDeleteStaff(RetrieveUpdateDestroyAPIView):
    """DOCSTRING"""
    # Set permission to request.user == objects.user
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
