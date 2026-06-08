from django.urls import path
from .views import (
    book_room,
    booking_history
)

urlpatterns = [

    path(
        'book/<int:room_id>/',
        book_room,
        name='book_room'
    ),

    path(
        'history/',
        booking_history,
        name='booking_history'
    ),

]