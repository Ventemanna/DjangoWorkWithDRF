from django.urls import path

from . import views

urlpatterns = [
    path('api/address/', views.GetAddressView.as_view()),
    path('api/supplier/', views.GetSupplierView.as_view()),
    path('api/product/', views.GetProductView.as_view()),
]