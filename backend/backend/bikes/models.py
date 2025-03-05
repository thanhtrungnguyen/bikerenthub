from django.db import models
from backend.common.models import BaseModel
from backend.stations.models import Station

class BikeType(models.TextChoices):
    STANDARD = 'standard', 'Standard'
    CARGO = 'cargo', 'Cargo'

class BikeStatus(models.TextChoices):
    AVAILABLE = 'available', 'Available'
    IN_USE = 'in_use', 'In Use'
    MAINTENANCE = 'maintenance', 'Maintenance'
    LOCKED = 'locked', 'Locked'

class Bike(BaseModel):
    station = models.ForeignKey(Station, null=True, on_delete=models.SET_NULL, related_name='bikes')
    bike_type = models.CharField(max_length=20, choices=BikeType.choices, default=BikeType.STANDARD)
    status = models.CharField(max_length=20, choices=BikeStatus.choices, default=BikeStatus.AVAILABLE)
    last_maintenance_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.bike_type} - {self.status}"
