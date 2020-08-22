from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers
from .permissions import IsCreationOrIsAuthenticated


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


# UUIDUser viewset
# - - - - - - - - - - - - - - - - - - -
class UUIDUserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsCreationOrIsAuthenticated, )
    # serializer_class = serializers.UUIDUserSimpleSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.UUIDUser.objects.all()
        return models.UUIDUser.objects.filter(group=self.request.user.group)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            if self.request.user.is_superuser:
                return serializers.UUIDUserSimpleSerializer
            return serializers.UUIDUserSimpleSerializer
        return serializers.UUIDUserCreateSerializer


# Auth token viewset
# - - - - - - - - - - - - - - - - - - -
class AuthToken(ObtainAuthToken):

    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        result = serializers.UUIDUserCreateSerializer(user)

        return Response(result.data)