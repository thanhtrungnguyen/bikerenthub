from django.utils.timezone import now
from django.db import transaction
from .models import Bike, BikeStatus, BikeType


@transaction.atomic
def bike_create(*, station=None, bike_type=BikeType.STANDARD):
    return Bike.objects.create(
        station=station,
        bike_type=bike_type,
        status=BikeStatus.AVAILABLE
    )

@transaction.atomic
def bike_update_status(*, bike, status):
    bike.status = status
    if status == BikeStatus.MAINTENANCE:
        bike.last_maintenance_at = now()
    bike.save(update_fields=['status', 'last_maintenance_at', 'updated_at'])
    return bike


@transaction.atomic
def lock_bike(bike: Bike):
    """
    Lock a bike after use or when returned to a station.
    """
    bike.status = BikeStatus.LOCKED
    bike.save(update_fields=['status', 'updated_at'])

@transaction.atomic
def unlock_bike(bike: Bike):
    """
    Unlock a bike for a new rental.
    """
    if bike.status not in [BikeStatus.AVAILABLE, BikeStatus.LOCKED]:
        raise ValueError(f"Cannot unlock bike in status {bike.status}")

    bike.status = BikeStatus.IN_USE
    bike.save(update_fields=['status', 'updated_at'])

@transaction.atomic
def mark_bike_as_maintenance(bike: Bike):
    """
    Put bike into maintenance mode.
    """
    bike.status = BikeStatus.MAINTENANCE
    bike.last_maintenance_at = now()
    bike.save(update_fields=['status', 'last_maintenance_at', 'updated_at'])
