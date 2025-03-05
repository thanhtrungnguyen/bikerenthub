from .models import Station, StationSlot
from .filters import StationFilter

from typing import Optional
from django.db.models import Prefetch

def get_stations(*, filters=None):
    filters = filters or {}
    qs = Station.objects.all()
    return StationFilter(filters, qs).qs

def get_station(*, station_id):
    return Station.objects.filter(id=station_id).first()


def get_station_with_slots_and_esps(station_id: int) -> Optional[Station]:
    """
    Fetch a station with preloaded slots and ESP devices.
    This does NOT format the data — just returns the model.
    """
    return (
        Station.objects.prefetch_related(
            Prefetch(
                'slots',
                queryset=StationSlot.objects.select_related('esp_device').order_by('slot_number')
            ),
            'esp_devices'
        )
        .filter(id=station_id)
        .first()
    )
