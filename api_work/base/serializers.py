from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)

class SupplierSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address_id = serializers.CharField(source='address.id',max_length=100)
    phone_number = serializers.CharField(max_length=7)