from rest_framework.routers import DefaultRouter
from ..api.views import ProductViewSets, ProductListCreateAPIView
from django.urls import path

productRouter = DefaultRouter()
productRouter.register(prefix='products', basename='products', viewset=ProductViewSets)

urlpatterns = [
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
