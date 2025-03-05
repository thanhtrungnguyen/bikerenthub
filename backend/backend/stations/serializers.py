from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'location', 'total_capacity', 'current_bikes', 'created_at', 'updated_at']
