from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.store.models import Product
from .serializers import ProductSerializer



class ProductAPIView(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["status"]
    search_fields = ["title", "description"]