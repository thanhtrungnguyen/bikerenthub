from rest_framework import serializers
from backend.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "is_active", "is_admin", "date_joined"]


class LoginSerializer(serializers.Serializer):
    """
    Validates login input (email & password).
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)


class RefreshSerializer(serializers.Serializer):
    """
    Validates the presence of the refresh token in cookies.
    """
    refresh_token = serializers.CharField()

    def validate_refresh_token(self, value):
        if not value:
            raise serializers.ValidationError("Refresh token is missing.")
        return value
