"""Views for Users."""

from django.contrib.auth import get_user_model

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
)

from core.rest.serializers.user import (
    UserListSerializer,
    UserDetailSerializer,
)


User = get_user_model()


class UserList(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserListSerializer
    queryset = User().get_all_actives()


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserDetailSerializer
    queryset = User().get_all_actives()
