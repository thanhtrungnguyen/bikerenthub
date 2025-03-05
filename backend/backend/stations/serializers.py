from rest_framework import serializers
from backend.stations.models import Station, ESPDevice


class ESPDeviceInputSerializer(serializers.Serializer):
    esp_id = serializers.CharField(max_length=50)
    ip_address = serializers.IPAddressField()


class StationCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    total_capacity = serializers.IntegerField()
    esp_devices = serializers.ListField(child=ESPDeviceInputSerializer())


class StationUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    total_capacity = serializers.IntegerField(required=False)


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'latitude', 'longitude', 'total_capacity', 'created_at', 'updated_at']
