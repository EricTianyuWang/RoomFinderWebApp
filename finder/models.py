from re import template
from django.db import models
from django.http import HttpResponse


class BUILDING(models.Model):
    BUILDING_NAME = models.CharField(max_length=255)
    BUILDING_CITY = models.CharField(max_length=255)
    BUILDING_ZIP = models.CharField(max_length=255)
    BUILDING_STREET = models.CharField(max_length=255)
    BUILDING_STATE = models.CharField(max_length=255)

class ROOM(models.Model):
    BUILDING_ID = models.ForeignKey(BUILDING, on_delete=models.CASCADE)
    ROOM_NUMBER =  models.CharField(max_length=255)
    CAPACITY = models.IntegerField()

class STUDENT(models.Model):
    STUDENT_LNAME = models.CharField(max_length=255)
    STUDENT_FNAME = models.CharField(max_length=255)
    STUDENT_LNAME = models.CharField(max_length=255)
    STUDENT_EMAIL = models.CharField(max_length=255)
    def __str__(self):
        return self.STUDENT_FNAME

class STUDENT_ROOM(models.Model):
    STUDENT_ID = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    ROOM_ID = models.ForeignKey(ROOM, on_delete=models.CASCADE)




