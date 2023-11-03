from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.user import models
from apps.user import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = AllowAny,
