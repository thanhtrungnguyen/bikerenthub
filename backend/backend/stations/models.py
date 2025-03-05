from django.contrib.gis.db import models as gis_models
from backend.common.models import BaseModel
from django.db import models

class Station(BaseModel):
    name = models.CharField(max_length=100)
    location = gis_models.PointField(geography=True)
    total_capacity = models.PositiveIntegerField()
    current_bikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
