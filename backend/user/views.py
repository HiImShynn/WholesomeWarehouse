"""DOCSTRING"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import StaffSerializer, PartnerSerializer, RegisterPartnerSerializer, RegisterStaffSerializer
from .permissions import StaffPermission
from .models import Staff, Partner

class ListStaff(APIView):
    """DOCSTRING"""
    permission_classes = [StaffPermission]

    def get(self, request):
        list_of_staffs = Staff.objects.all()
        serializer = StaffSerializer(list_of_staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListPartner(APIView):
    """DOCSTRING"""
    permission_classes = [StaffPermission]

    def get(self, request):
        list_of_partners = Partner.objects.all()
        serializer = PartnerSerializer(list_of_partners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# CreateAPIView -> Create Partner


class CreatePartner(CreateAPIView):
    """DOCSTRING"""
    permission_classes = [IsAdminUser]
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class CreateStaff(CreateAPIView):
    """DOCSTRING"""
    permission_classes = [IsAdminUser]
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


class StaffCreate(APIView):
    """DS"""
    permission_classes = [AllowAny]

    def post(self, request):
        """DS"""
        reg_serializer = RegisterStaffSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_partner = reg_serializer.save()
            if new_partner:
                return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartnerCreate(APIView):
    """DS"""
    permission_classes = [AllowAny]

    def post(self, request):
        """DS"""
        reg_serializer = RegisterPartnerSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_partner = reg_serializer.save()
            if new_partner:
                return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
