from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import *
from .serializers import AddressSerializer, SupplierSerializer

class GetAddressView(APIView):
    def get(self, request):
        queryset = Address.objects.all()
        serializer_for_queryset = AddressSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)

class GetSupplierView(APIView):
    def get(self, request):
        queryset = Supplier.objects.all()
        serializer_for_queryset = SupplierSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)