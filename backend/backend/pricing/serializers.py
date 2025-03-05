from rest_framework import serializers
from .models import DynamicPricing

class DynamicPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicPricing
        fields = [
            'id', 'bike_type', 'time_of_day', 'day_of_week', 'weather_condition',
            'base_price', 'ai_adjusted_price', 'created_at', 'updated_at'
        ]
