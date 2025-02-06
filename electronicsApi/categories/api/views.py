from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializers
from ..models import Category


class CategoryViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
