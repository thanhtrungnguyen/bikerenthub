from django.urls import path
from .apis import BookingListApi, BookingDetailApi, BookingCreateApi, BookingCompleteApi

urlpatterns = [
    path('', BookingListApi.as_view(), name='booking-list'),
    path('<uuid:booking_id>/', BookingDetailApi.as_view(), name='booking-detail'),
    path('create/', BookingCreateApi.as_view(), name='booking-create'),
    path('<uuid:booking_id>/complete/', BookingCompleteApi.as_view(), name='booking-complete'),
]
