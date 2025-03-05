from django.urls import path
from .apis import BookingListApi, BookingDetailApi, BookingCreateApi, BookingCompleteApi

app_name = 'bookings'

urlpatterns = [
    path('', BookingListApi.as_view(), name='booking-list'),
    path('<int:booking_id>/', BookingDetailApi.as_view(), name='booking-detail'),
    path('create/', BookingCreateApi.as_view(), name='booking-create'),
    path('<int:booking_id>/complete/', BookingCompleteApi.as_view(), name='booking-complete'),
]
