from rest_framework import serializers
from .models import Booking, Payment

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'bike', 'pickup_station', 'return_station',
            'start_time', 'end_time', 'status', 'price_per_minute', 'total_price'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'user', 'amount', 'payment_status', 'transaction_id']
