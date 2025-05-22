from django.db.models import F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import AddressSerializer, SupplierSerializer, ProductSerializer, ClientSerializer, CountSerializer, \
    ImageSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['patch', 'put'])
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

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        if "image" not in request.data:
            return Response({"error": "No image provided"}, status=400)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = Image.objects.create(**serializer.validated_data)
            image.save()
            return Response(ImageSerializer(image).data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        try:
            image = Image.objects.get(pk=str(product.image_id))
        except Image.DoesNotExist:
            return Response({"error": "Image not found"}, status=404)

        return Response(ImageSerializer(image).data)

    @action(detail=True, methods=['put', 'post', 'patch', 'get'])
    def update_product_image(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        if "image" not in request.data:
            return Response({"error": "No image provided"}, status=400)

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            if product.image_id:
                image, _ = Image.objects.update_or_create(
                    id=str(product.image_id),
                    defaults=serializer.validated_data,
                )
                image.save()
            else:
                image = Image.objects.create(**serializer.validated_data)
                product.image_id = image
                product.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=400)