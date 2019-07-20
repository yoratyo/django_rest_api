from rest_framework import  viewsets, permissions
from .models import Product, ProductType, Customer
from .serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductTypeView(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # Custom permission class
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
