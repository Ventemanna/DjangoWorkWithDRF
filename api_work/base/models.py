import uuid

from django.db import models

class Address(models.Model):
    id = models.AutoField(primary_key=True, null=False)
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

class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.BinaryField()

    def __str__(self):
        return f"{self.id}"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Client(models.Model):
    genders = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другое'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=120)
    client_surname = models.CharField(max_length=120)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=genders)
    registration_date = models.DateField(auto_now_add=True)
    address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.client_name} {self.client_surname}"