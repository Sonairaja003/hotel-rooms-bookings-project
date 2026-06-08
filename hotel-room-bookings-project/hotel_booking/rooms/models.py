from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return self.room_name