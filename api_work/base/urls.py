from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'address', views.AddressViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'image', views.ImageViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]