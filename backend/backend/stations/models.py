
from backend.common.models import BaseModel
from django.db import models

class Station(BaseModel):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    total_capacity = models.PositiveIntegerField()
    current_bikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
