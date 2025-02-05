from rest_framework.routers import DefaultRouter
from django.urls import path
from ..api.views import UserApiViewSets, UserViewSets

userRouter = DefaultRouter()
userRouter.register(prefix='user', basename='user', viewset=UserViewSets)

urlpatterns = [
    path('me/', UserApiViewSets.as_view())
]