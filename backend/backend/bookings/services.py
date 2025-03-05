from django.utils.timezone import now
from django.db import transaction
from .models import Booking, Payment, BookingStatus
from backend.pricing.services import calculate_price
from backend.bikes.services import unlock_bike, lock_bike
from ..bikes.models import BikeStatus, Bike


@transaction.atomic
def create_booking(*, user, bike, pickup_station, price_per_minute):
    unlock_bike(bike)

    booking = Booking.objects.create(
        user=user,
        bike=bike,
        pickup_station=pickup_station,
        start_time=now(),
        status=BookingStatus.ACTIVE,
        price_per_minute=price_per_minute,
    )
    return booking

@transaction.atomic
def complete_booking(*, booking, return_station):
    booking.end_time = now()
    booking.status = BookingStatus.COMPLETED
    booking.return_station = return_station

    total_minutes = (booking.end_time - booking.start_time).total_seconds() / 60
    booking.total_price = round(total_minutes * booking.price_per_minute, 2)

    lock_bike(booking.bike)
    booking.save()

    return booking

@transaction.atomic
def cancel_booking(*, booking):
    booking.status = BookingStatus.CANCELED
    lock_bike(booking.bike)
    booking.save()
    return booking

