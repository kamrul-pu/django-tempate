"""Serializer for user model."""

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import serializers

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
            "avatar",
        )
        read_only_fields = ("id", "uid")


class UserDetailSerializer(UserListSerializer):
    class Meta(UserListSerializer.Meta):
        fields = UserListSerializer.Meta.fields + (
            "status",
            "is_staff",
            "organization",
            "phone",
        )
        read_only_fields = UserListSerializer.Meta.read_only_fields + ()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate_password(self, value):
        password = value
        confirm_password = self.initial_data.get("confirm_password", "")
        if password != confirm_password:
            raise serializers.ValidationError(
                detail="Password and confirm password don't match!!!",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return value

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "gender",
            "avatar",
            "password",
            "confirm_password",
        )

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        user = User(**validated_data)
        user.set_password(validated_data.get("password", ""))
        user.save()
        return user


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "first_name",
            "last_name",
            "phone",
            "email",
            "gender",
            "avatar",
            "organization",
            "kind",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "uid",
            "created_at",
            "updated_at",
        )
