from django.db import models

# Create your models here.
from django.db import models
from backend.common.models import BaseModel
from backend.bikes.models import Bike

class MaintenanceType(models.TextChoices):
    INSPECTION = 'inspection', 'Inspection'
    REPAIR = 'repair', 'Repair'
    DOCK_REPAIR = 'dock_repair', 'Dock Repair'

class MaintenanceLog(BaseModel):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=50, choices=MaintenanceType.choices)
    description = models.TextField()
    performed_by = models.CharField(max_length=100)
    maintenance_date = models.DateTimeField()
