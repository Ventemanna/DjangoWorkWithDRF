import uuid

from django.db import models
from django.conf import settings

# Create your models here.

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=120)
    street = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}"

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name}"
