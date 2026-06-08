from django.shortcuts import render, get_object_or_404
from .models import Room


def room_list(request):

    rooms = Room.objects.all()

    return render(request, 'index.html', {
        'rooms': rooms
    })


def room_detail(request, id):

    room = get_object_or_404(Room, id=id)

    return render(request, 'room_detail.html', {
        'room': room
    })
from .forms import RoomForm
from django.shortcuts import render, redirect

def add_room(request):

    if request.method == 'POST':

        form = RoomForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('manage_rooms')

    else:

        form = RoomForm()

    return render(
        request,
        'add_room.html',
        {
            'form': form
        }
    )
from .models import Room

def manage_rooms(request):

    rooms = Room.objects.all()

    return render(
        request,
        'manage_rooms.html',
        {
            'rooms': rooms
        }
    )
from django.shortcuts import get_object_or_404

def delete_room(request, room_id):

    room = get_object_or_404(
        Room,
        id=room_id
    )

    room.delete()

    return redirect(
        'manage_rooms'
    )
def edit_room(request, room_id):

    room = get_object_or_404(
        Room,
        id=room_id
    )

    if request.method == 'POST':

        form = RoomForm(
            request.POST,
            request.FILES,
            instance=room
        )

        if form.is_valid():

            form.save()

            return redirect(
                'manage_rooms'
            )

    else:

        form = RoomForm(
            instance=room
        )

    return render(
        request,
        'edit_room.html',
        {
            'form': form
        }
    )
from bookings.models import Booking

def manage_bookings(request):

    bookings = Booking.objects.all().order_by('-id')

    return render(
        request,
        'manage_bookings.html',
        {
            'bookings': bookings
        }
    )
from django.contrib.auth.models import User

def manage_users(request):

    users = User.objects.all()

    return render(
        request,
        'manage_users.html',
        {
            'users': users
        }
    )