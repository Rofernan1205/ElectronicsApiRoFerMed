from rest_framework.routers import DefaultRouter
from .views import CategoryViewSets

categoryRouter = DefaultRouter()
categoryRouter.register(prefix="categories", basename="categories",viewset=CategoryViewSets )