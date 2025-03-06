from typing import Dict, Any
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.stations.services import create_station, update_station, get_station_detail_response
from backend.stations.models import Station
from backend.stations.serializers import StationSerializer, StationCreateSerializer, StationUpdateSerializer
from django.http import Http404


class StationListApi(APIView):
    """
    GET: List all stations.
    POST: Create a new station with ESP devices.
    """

    def get(self, request) -> Response:
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

class StationCreateApi(APIView):
    def post(self, request) -> Response:
        serializer = StationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        station = create_station(
            name=serializer.validated_data['name'],
            latitude=serializer.validated_data['latitude'],
            longitude=serializer.validated_data['longitude'],
            total_capacity=serializer.validated_data['total_capacity'],
            esp_devices_data=serializer.validated_data['esp_devices']
        )

        return Response(StationSerializer(station).data, status=status.HTTP_201_CREATED)


class StationGetByIdApi(APIView):

    def get_object(self, station_id: int) -> Station:
        try:
            return Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            raise Http404("Station not found")




class StationRetrieveUpdateApi(APIView):
    """
    GET: Retrieve station details.
    PUT: Update station details (including capacity adjustment).
    """

    def put(self, request, station_id: int) -> Response:
        station = self.get_object(station_id)

        serializer = StationUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_station = update_station(
            station=station,
            name=serializer.validated_data.get('name'),
            latitude=serializer.validated_data.get('latitude'),
            longitude=serializer.validated_data.get('longitude'),
            total_capacity=serializer.validated_data.get('total_capacity')
        )

        return Response(StationSerializer(updated_station).data)

class StationDetailApi(APIView):
    def get(self, request, station_id: int) -> Response:
        station_detail = get_station_detail_response(station_id)

        if station_detail is None:
            raise Http404("Station not found")

        return Response(station_detail)
