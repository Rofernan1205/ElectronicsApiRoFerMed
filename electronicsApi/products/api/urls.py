from rest_framework.routers import DefaultRouter
from ..api.views import ProductViewSets

productRouter = DefaultRouter()
productRouter.register(prefix='products', basename='products', viewset=ProductViewSets)