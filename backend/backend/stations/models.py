from django.db import models
from backend.common.models import BaseModel

class Station(BaseModel):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class ESPDevice(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="esp_devices")
    esp_id = models.CharField(max_length=50, unique=True)  # ESP ID (like "esp8266-1")
    ip_address = models.GenericIPAddressField()

class SlotStatus(models.TextChoices):
    AVAILABLE = 'available', 'Available'
    OCCUPIED = 'occupied', 'Occupied'
    RESERVED = 'reserved', 'Reserved'
    MAINTENANCE = 'maintenance', 'Maintenance'

class StationSlot(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='slots')
    esp_device = models.ForeignKey(ESPDevice, on_delete=models.CASCADE, related_name='slots')
    slot_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=SlotStatus.choices, default=SlotStatus.AVAILABLE)
    bike = models.OneToOneField('bikes.Bike', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('station', 'slot_number')

