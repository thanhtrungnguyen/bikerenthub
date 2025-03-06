from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from backend.authentication.serializers import (
    UserSerializer,
    LoginSerializer,
    RefreshSerializer,
)
from django.contrib.auth import authenticate


class CookieBasedLoginApi(APIView):
    """
    Login API that returns access token in response and refresh token in HttpOnly cookie.
    """

    authentication_classes = []  # Important - No auth required for login
    permission_classes = []      # Important - Public access to login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({"error": "User account is inactive"}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)

        response = Response({
            "access": str(refresh.access_token),
        })

        response.set_cookie(
            settings.SIMPLE_JWT["AUTH_COOKIE"],
            str(refresh),
            httponly=settings.SIMPLE_JWT.get("AUTH_COOKIE_HTTP_ONLY", True),
            samesite=settings.SIMPLE_JWT.get("AUTH_COOKIE_SAMESITE", "Lax"),
            secure=settings.SIMPLE_JWT.get("AUTH_COOKIE_SECURE", False),
            path="/api/auth/refresh/"
        )

        return response


class CookieBasedTokenRefreshApi(APIView):
    """
    Refresh access token using HttpOnly cookie.
    """

    def post(self, request):
        serializer = RefreshSerializer(data=request.COOKIES)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh_token"]

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({"access": access_token})
        except Exception:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_401_UNAUTHORIZED)


class CookieBasedLogoutApi(APIView):
    """
    Clear refresh token cookie (logout).
    """

    def post(self, request):
        response = Response({"detail": "Logged out"})
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"])
        return response


class CurrentUserApi(APIView):
    """
    Get current logged-in user profile.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
