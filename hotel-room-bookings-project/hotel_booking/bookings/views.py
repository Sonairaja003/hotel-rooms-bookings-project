from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from rooms.models import Room
from .models import Booking

def book_room(request, room_id):

    room = Room.objects.get(id=room_id)

    form = BookingForm()

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.room = room

            booking.save()

            return redirect('/')

    return render(request,
                  'booking.html',
                  {
                      'form': form,
                      'room': room
                  })

def booking_history(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request,
                  'booking_history.html',
                  {
                      'bookings': bookings
                  })