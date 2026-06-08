from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = [
        'room_name',
        'price',
        'available'
    ]

    search_fields = [
        'room_name'
    ]

    list_filter = [
        'available'
    ]