from django.urls import path
from .views import room_list, room_detail
from .views import add_room
from .views import manage_rooms
from .views import delete_room
from .views import edit_room
from .views import manage_bookings
from .views import manage_users

urlpatterns = [

    path('', room_list, name='home'),

    path('room/<int:id>/', room_detail, name='room_detail'),
    path(
    'add-room/',
    add_room,
    name='add_room'
),
path(
    'manage-rooms/',
    manage_rooms,
    name='manage_rooms'
),
path(
    'delete-room/<int:room_id>/',
    delete_room,
    name='delete_room'
),
path(
    'edit-room/<int:room_id>/',
    edit_room,
    name='edit_room'
),
path(
    'manage-bookings/',
    manage_bookings,
    name='manage_bookings'
),
path(
    'manage-users/',
    manage_users,
    name='manage_users'
),

]