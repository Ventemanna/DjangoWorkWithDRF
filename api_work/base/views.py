from django.db.models import F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .pagination import SimpleOptionalPagination

from .models import *
from .serializers import AddressSerializer, SupplierSerializer, ProductSerializer, ClientSerializer, CountSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['patch'])
    def address(self, request, pk=None):
        supplier = self.get_object()
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address, _ = Address.objects.update_or_create(
                id=supplier.address_id,
                defaults=serializer.validated_data,
            )
            supplier.address = address
            supplier.save()
            return Response(SupplierSerializer(supplier).data)

        return Response(serializer.errors, status=400)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['patch'])
    def purchase(self, request, pk=None):
        product = self.get_object()
        serializer = CountSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        count = serializer.validated_data['count']
        if product.available_stock < count:
            return Response({"error": "Not enough products in stock"}, status=400)
        Product.objects.filter(id=product.id).update(available_stock=F('available_stock') - count)
        product.refresh_from_db()
        return Response(ProductSerializer(product).data)

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        queryset = Client.objects.all()
        name = self.request.query_params.get('name')
        surname = self.request.query_params.get('surname')
        if name:
            queryset = queryset.filter(client_name__icontains=name)
        if surname:
            queryset = queryset.filter(client_surname__icontains=surname)
        return queryset

    @action(detail=True, methods=['patch'])
    def address(self, request, pk=None):
        client = self.get_object()
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            address, _ = Address.objects.update_or_create(
                id=client.address_id_id,
                defaults=serializer.validated_data
            )
            client.address_id = address
            client.save()

            return Response(ClientSerializer(client).data)

        return Response(serializer.errors, status=400)