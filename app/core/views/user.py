"""Views for Users."""

from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
)

from common.choices import Status

from core.serializers.user import (
    UserListSerializer,
    UserDetailSerializer,
    UserRegistrationSerializer,
    MeSerializer,
)

User = get_user_model()


class UserList(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserListSerializer
    queryset = User.objects.filter(status=Status.ACTIVE).order_by("-pk")


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(status=Status.ACTIVE).order_by("-pk")
    lookup_field = "uid"


class UserRegistration(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer


class MeDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
