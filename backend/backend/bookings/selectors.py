from .models import Booking, Payment

def get_booking(*, booking_id):
    return Booking.objects.filter(id=booking_id).first()

def get_user_bookings(*, user_id):
    return Booking.objects.filter(user_id=user_id).order_by('-start_time')

def get_booking_payment(*, booking_id):
    return Payment.objects.filter(booking_id=booking_id).first()
