"""Serializer for user model."""

from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "first_name",
            "last_name",
            "email",
            "gender",
            "kind",
            "image",
        )
        read_only_fields = ("id", "uid")


class UserDetailSerializer(UserListSerializer):
    class Meta(UserListSerializer.Meta):
        fields = UserListSerializer.Meta.fields + (
            "status",
            "is_staff",
        )
        read_only_fields = UserListSerializer.Meta.read_only_fields + ()
