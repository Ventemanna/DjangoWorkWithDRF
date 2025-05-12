from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/address', views.AddressViewSet)
router.register(r'api/product', views.ProductViewSet)
router.register(r'api/supplier', views.SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]