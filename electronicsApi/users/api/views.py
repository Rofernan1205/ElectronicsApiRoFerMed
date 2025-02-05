from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import views
from .serializers import UserSerializers
from ..models import User


class UserViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]  # Usuarios administradores
    serializer_class = UserSerializers
    queryset = User.objects.all()

    # Encriptar password

    def create(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data["password"]
        if password:
            request.data["password"] = make_password(password)
        else:
            request.data["password"] = request.user.password
        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        password = request.data["password"]
        if password:
            request.data["password"] = make_password(password)
        else:
            request.data["password"] = request.user.password
        return super().update(request, *args, **kwargs)


class UserApiViewSets(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializers(request.user)
        return Response(serializer.data)
