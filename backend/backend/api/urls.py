from django.urls import include, path

app_name = 'api'
urlpatterns = [
    path("auth/", include("backend.authentication.urls", "authentication")),
    path("users/", include("backend.users.urls", "users")),
    path("errors/", include("backend.errors.urls", "errors")),
    path("files/", include("backend.files.urls", "files")),
    path("bikes/", include("backend.bikes.urls", "bikes")),
    path("stations/", include("backend.stations.urls", "stations")),
    path("bookings/", include("backend.bookings.urls", "bookings")),
    path("pricing/", include("backend.pricing.urls", "pricing")),
    # path("se/", include("backend..urls", "files")),
    # path("files/", include("backend.files.urls", "files")),
    # path("files/", include("backend.files.urls", "files")),
]
