from django.db import models
from backend.common.models import BaseModel

class DynamicPricing(BaseModel):
    bike_type = models.CharField(max_length=50)
    time_of_day = models.CharField(max_length=10, null=True, blank=True)  # morning, afternoon, evening
    day_of_week = models.PositiveSmallIntegerField(null=True, blank=True)  # 0=Monday, 6=Sunday
    weather_condition = models.CharField(max_length=50, null=True, blank=True)  # clear, rain, snow, etc.
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    ai_adjusted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = [
            ('bike_type', 'time_of_day', 'day_of_week', 'weather_condition')
        ]
