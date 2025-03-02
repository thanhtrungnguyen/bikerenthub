from django.urls import include, path

app_name = 'api'
urlpatterns = [
    path("auth/", include("backend.authentication.urls", "authentication")),
    path("users/", include("backend.users.urls", "users")),
    path("errors/", include("backend.errors.urls", "errors")),
    path("files/", include("backend.files.urls", "files"))
]
