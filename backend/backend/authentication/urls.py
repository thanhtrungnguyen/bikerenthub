from django.urls import path
from backend.authentication.apis import (
    CookieBasedLoginApi,
    CookieBasedTokenRefreshApi,
    CookieBasedLogoutApi,
    CurrentUserApi
)

app_name = 'authentication'

urlpatterns = [
    path("login/", CookieBasedLoginApi.as_view(), name="cookie_login"),
    path("refresh/", CookieBasedTokenRefreshApi.as_view(), name="cookie_refresh"),
    path("logout/", CookieBasedLogoutApi.as_view(), name="cookie_logout"),
    path("me/", CurrentUserApi.as_view(), name="current_user"),
]
