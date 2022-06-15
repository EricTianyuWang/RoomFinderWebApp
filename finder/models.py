# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#    Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Availability(models.Model):
    availability_id = models.AutoField(db_column='AVAILABILITY_ID', primary_key=True)  # Field name made lowercase.
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='ROOM_ID')  # Field name made lowercase.
    available_day = models.CharField(db_column='AVAILABLE_DAY', max_length=255)  # Field name made lowercase.
    time = models.ForeignKey('TimeBlock', models.DO_NOTHING, db_column='TIME_ID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'availability'


class Building(models.Model):
    building_id = models.AutoField(db_column='BUILDING_ID', primary_key=True)  # Field name made lowercase.
    building_name = models.CharField(db_column='BUILDING_NAME', max_length=255)  # Field name made lowercase.
    building_city = models.CharField(db_column='BUILDING_CITY', max_length=255)  # Field name made lowercase.
    building_zip = models.CharField(db_column='BUILDING_ZIP', max_length=255)  # Field name made lowercase.
    building_street = models.CharField(db_column='BUILDING_STREET', max_length=255)  # Field name made lowercase.
    building_state = models.CharField(db_column='BUILDING_STATE', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'building'





class FinderBuilding(models.Model):
    id = models.BigAutoField(primary_key=True)
    building_name = models.CharField(db_column='BUILDING_NAME', max_length=255)  # Field name made lowercase.
    building_city = models.CharField(db_column='BUILDING_CITY', max_length=255)  # Field name made lowercase.
    building_zip = models.CharField(db_column='BUILDING_ZIP', max_length=255)  # Field name made lowercase.
    building_street = models.CharField(db_column='BUILDING_STREET', max_length=255)  # Field name made lowercase.
    building_state = models.CharField(db_column='BUILDING_STATE', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'finder_building'


class FinderRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_number = models.CharField(db_column='ROOM_NUMBER', max_length=255)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='CAPACITY')  # Field name made lowercase.
    building_id = models.ForeignKey(FinderBuilding, models.DO_NOTHING, db_column='BUILDING_ID_id')  # Field name made lowercase.

    class Meta:
        
        db_table = 'finder_room'


class FinderStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_fname = models.CharField(db_column='STUDENT_FNAME', max_length=255)  # Field name made lowercase.
    student_lname = models.CharField(db_column='STUDENT_LNAME', max_length=255)  # Field name made lowercase.
    student_email = models.CharField(db_column='STUDENT_EMAIL', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'finder_student'


class FinderStudentRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.ForeignKey(FinderRoom, models.DO_NOTHING, db_column='ROOM_ID_id')  # Field name made lowercase.
    student_id = models.ForeignKey(FinderStudent, models.DO_NOTHING, db_column='STUDENT_ID_id')  # Field name made lowercase.

    class Meta:
        
        db_table = 'finder_student_room'


class Rating(models.Model):
    rating_id = models.AutoField(db_column='RATING_ID', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='STUDENT_ID')  # Field name made lowercase.
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='ROOM_ID')  # Field name made lowercase.
    rating_score = models.IntegerField(db_column='RATING_SCORE')  # Field name made lowercase.

    class Meta:
        
        db_table = 'rating'


class Reservation(models.Model):
    reservation_id = models.AutoField(db_column='RESERVATION_ID', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='STUDENT_ID')  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    reservation_date = models.CharField(db_column='RESERVATION_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.ForeignKey('TimeBlock', models.DO_NOTHING, db_column='TIME_ID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'reservation'


class Room(models.Model):
    room_id = models.AutoField(db_column='ROOM_ID', primary_key=True)  # Field name made lowercase.
    building = models.ForeignKey(Building, models.DO_NOTHING, db_column='BUILDING_ID')  # Field name made lowercase.
    room_number = models.CharField(db_column='ROOM_NUMBER', max_length=255)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='CAPACITY')  # Field name made lowercase.

    class Meta:
        
        db_table = 'room'


class Student(models.Model):
    student_id = models.AutoField(db_column='STUDENT_ID', primary_key=True)  # Field name made lowercase.
    student_fname = models.CharField(db_column='STUDENT_FNAME', max_length=255)  # Field name made lowercase.
    student_lname = models.CharField(db_column='STUDENT_LNAME', max_length=255)  # Field name made lowercase.
    student_email = models.CharField(db_column='STUDENT_EMAIL', max_length=255)  # Field name made lowercase.

    class Meta:
        
        db_table = 'student'


class StudentRoom(models.Model):
    student = models.OneToOneField(Student, models.DO_NOTHING, db_column='STUDENT_ID', primary_key=True)  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='ROOM_ID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'student_room'
        unique_together = (('student', 'room'),)


class TimeBlock(models.Model):
    time_id = models.AutoField(db_column='TIME_ID', primary_key=True)  # Field name made lowercase.
    start_time = models.CharField(db_column='START_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'time_block'
