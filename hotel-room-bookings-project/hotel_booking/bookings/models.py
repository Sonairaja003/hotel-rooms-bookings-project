from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room


class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.IntegerField(default=1)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.room.room_name}"