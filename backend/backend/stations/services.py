from django.db import transaction
from .models import Station

@transaction.atomic
def update_bike_count(*, station: Station, count_change: int):
    """
    Increment or decrement the bike count for a station.
    """
    station.current_bikes = max(0, station.current_bikes + count_change)
    station.save(update_fields=['current_bikes', 'updated_at'])
    return station
