from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=200)
    visible = models.IntegerField(default=1)
    def __str__(self):
        return self.room_name
