from django.db import transaction
from typing import List, Dict, Optional, Any

from .models import Station

from django.db import transaction
from backend.stations.models import Station, StationSlot, ESPDevice, SlotStatus
from django.utils.timezone import now

from .selectors import get_station_with_slots_and_esps, get_stations


@transaction.atomic
def create_station(
    name: str,
    latitude: float,
    longitude: float,
    total_capacity: int,
    esp_devices_data: List[Dict[str, str]]
) -> Station:
    """
    Create a station with pre-defined slots and associated ESP devices.

    esp_devices_data should be a list of dicts like:
    [
        {"esp_id": "esp-001", "ip_address": "192.168.1.101"},
        {"esp_id": "esp-002", "ip_address": "192.168.1.102"},
    ]
    """
    station = Station.objects.create(
        name=name,
        latitude=latitude,
        longitude=longitude,
        total_capacity=total_capacity
    )

    # Create ESP devices
    esp_devices: List[ESPDevice] = []
    for esp_data in esp_devices_data:
        esp_device = ESPDevice.objects.create(
            station=station,
            esp_id=esp_data['esp_id'],
            ip_address=esp_data['ip_address']
        )
        esp_devices.append(esp_device)

    # Assign slots evenly across ESPs
    slots_per_esp: int = (total_capacity // len(esp_devices)) + 1
    slot_count: int = 0

    for esp_device in esp_devices:
        for _ in range(slots_per_esp):
            slot_number: int = slot_count + 1
            if slot_number > total_capacity:
                break

            StationSlot.objects.create(
                station=station,
                esp_device=esp_device,
                slot_number=slot_number,
                status=SlotStatus.AVAILABLE
            )
            slot_count += 1

    return station


@transaction.atomic
def update_station(
    station: Station,
    name: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    total_capacity: Optional[int] = None
) -> Station:
    """
    Update station details, including dynamically adjusting slots if total capacity changes.
    """

    if name:
        station.name = name
    if latitude is not None:
        station.latitude = latitude
    if longitude is not None:
        station.longitude = longitude

    if total_capacity is not None and total_capacity != station.total_capacity:
        if total_capacity > station.total_capacity:
            # Add new slots if capacity increased
            for slot_number in range(station.total_capacity + 1, total_capacity + 1):
                StationSlot.objects.create(
                    station=station,
                    slot_number=slot_number,
                    status=SlotStatus.AVAILABLE
                )
        elif total_capacity < station.total_capacity:
            # Optional: Remove excess slots if the station shrinks (only if slots are available)
            StationSlot.objects.filter(
                station=station,
                slot_number__gt=total_capacity,
                status=SlotStatus.AVAILABLE
            ).delete()

        station.total_capacity = total_capacity

    station.updated_at = now()
    station.save()

    return station

def get_station_list():
    return get_stations()


def get_station_detail_response(station_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetches a station and assembles detailed response including slots and ESP devices.
    This is where business logic lives.
    """
    station = get_station_with_slots_and_esps(station_id)
    if station is None:
        return None

    slots = [
        {
            "slot_number": slot.slot_number,
            "status": slot.status,
            "bike_id": str(slot.bike.id) if slot.bike else None,
            "esp_id": slot.esp_device.esp_id if slot.esp_device else None,
            "esp_ip": slot.esp_device.ip_address if slot.esp_device else None
        }
        for slot in station.slots.all()
    ]

    esp_devices = [
        {
            "esp_id": esp.esp_id,
            "ip_address": esp.ip_address
        }
        for esp in station.esp_devices.all()
    ]

    return {
        "station_id": station.id,
        "name": station.name,
        "latitude": float(station.latitude),
        "longitude": float(station.longitude),
        "slots": slots,
        "esp_devices": esp_devices
    }

