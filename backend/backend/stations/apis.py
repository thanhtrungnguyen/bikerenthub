from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.http import Http404
from .selectors import station_list, station_get
from .services import update_bike_count
from .serializers import StationSerializer

class StationListApi(APIView):
    def get(self, request):
        filters = request.query_params.dict()
        stations = station_list(filters=filters)
        data = StationSerializer(stations, many=True).data
        return Response(data)

class StationDetailApi(APIView):
    def get_object(self, station_id):
        station = station_get(station_id=station_id)
        if station is None:
            raise Http404
        return station

    def get(self, request, station_id):
        station = self.get_object(station_id)
        data = StationSerializer(station).data
        return Response(data)

class StationUpdateBikeCountApi(APIView):
    class InputSerializer(serializers.Serializer):
        count_change = serializers.IntegerField()

    def post(self, request, station_id):
        station = station_get(station_id=station_id)
        if station is None:
            raise Http404

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_station = update_bike_count(
            station=station,
            count_change=serializer.validated_data['count_change']
        )
        return Response(StationSerializer(updated_station).data)
