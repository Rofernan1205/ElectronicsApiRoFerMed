from rest_framework import viewsets, generics
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from ..models import Product


class ProductViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category "]


