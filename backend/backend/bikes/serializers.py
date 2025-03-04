from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'station', 'bike_type', 'status', 'last_maintenance_at', 'created_at', 'updated_at']
