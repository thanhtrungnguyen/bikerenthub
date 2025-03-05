from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from django.http import Http404
from .selectors import get_booking, get_user_bookings, get_booking_payment
from .services import create_booking, complete_booking, cancel_booking
from .serializers import BookingSerializer, PaymentSerializer
from backend.pricing.services import calculate_price

class BookingListApi(APIView):
    def get(self, request):
        user = request.user
        bookings = get_user_bookings(user_id=user.id)
        data = BookingSerializer(bookings, many=True).data
        return Response(data)

class BookingDetailApi(APIView):
    def get_object(self, booking_id):
        booking = get_booking(booking_id=booking_id)
        if not booking:
            raise Http404
        return booking

    def get(self, request, booking_id):
        booking = self.get_object(booking_id)
        data = BookingSerializer(booking).data
        return Response(data)

class BookingCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        bike_id = serializers.UUIDField()
        pickup_station_id = serializers.UUIDField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Calculate price (you can add dynamic price lookup)
        price_per_minute = calculate_price(
            bike_type='standard',  # Replace with actual type from bike model
            time_of_day='morning',  # Replace with time logic
            day_of_week=now().weekday(),
        )

        booking = create_booking(
            user=request.user,
            bike_id=serializer.validated_data['bike_id'],
            pickup_station_id=serializer.validated_data['pickup_station_id'],
            price_per_minute=price_per_minute
        )
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class BookingCompleteApi(APIView):
    class InputSerializer(serializers.Serializer):
        return_station_id = serializers.UUIDField()

    def post(self, request, booking_id):
        booking = get_booking(booking_id=booking_id)
        if not booking:
            raise Http404

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_booking = complete_booking(
            booking=booking,
            return_station_id=serializer.validated_data['return_station_id']
        )

        return Response(BookingSerializer(updated_booking).data)
