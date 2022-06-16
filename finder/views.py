from django.shortcuts import render
from .models import Student, Room, TimeBlock
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from datetime import datetime

def index(request):
    user_clicked_search = False
    rooms_found = ""
    time_searched = ""
    day_searched = ""
    reservation_room = ""
    reservation_time = ""
    if "time_searched" in request.POST and "day_searched" in request.POST:
        user_clicked_search = True
        day_searched = request.POST["day_searched"]
        time_searched = request.POST["time_searched"]
        rooms_found = Room.objects.raw(
            f"""
            SELECT 
                TIME_BLOCK.TIME_ID,
                TIME_BLOCK.START_TIME,
                AVAILROOM.AVAILABILITY_ID,
                AVAILROOM.ROOM_ID,
                AVAILROOM.ROOM_NUMBER,
                AVAILROOM.AVAILABLE_DAY
            FROM
                TIME_BLOCK
            INNER JOIN
                (SELECT 
                    AVAILABILITY.TIME_ID,
                    AVAILABILITY.AVAILABILITY_ID,
                    AVAILABILITY.AVAILABLE_DAY,
                    ROOM.ROOM_ID,
                    ROOM.ROOM_NUMBER
                FROM
                    AVAILABILITY
                INNER JOIN ROOM
                WHERE AVAILABILITY.ROOM_ID = ROOM.ROOM_ID) AS AVAILROOM ON TIME_BLOCK.TIME_ID = AVAILROOM.TIME_ID
            WHERE TIME_BLOCK.START_TIME = '{time_searched}' AND AVAILROOM.AVAILABLE_DAY = '{day_searched}';
            """
        )
    reserved_day = ""
    if "reservation_room" in request.POST and "reservation_time" in request.POST and "student_email" in request.POST and "reserved_day" in request.POST:
        reserved_day = request.POST["reserved_day"]
        reservation_room =  request.POST["reservation_room"]
        reservation_time =  request.POST["reservation_time"]
        student_email = request.POST["student_email"]
        student_id = ""
        students = Student.objects.raw(f"SELECT STUDENT_ID FROM STUDENT WHERE STUDENT_EMAIL LIKE '{student_email}'")
        for s in students:
            student_id = s.student_id
        print("------------------------------------------------------------------------", request.POST["student_email"])
        print("sID", student_id)
        rooms = Room.objects.raw(f"SELECT ROOM_ID FROM ROOM WHERE ROOM.ROOM_NUMBER LIKE '{reservation_room}'")
        room_id = ""
        for a in rooms:
            room_id = a.room_id

        #curDT = datetime.now()
        #reservation_date = curDT.strftime("%m/%d/%Y")

        times = TimeBlock.objects.raw(f"SELECT TIME_ID FROM TIME_BLOCK WHERE TIME_BLOCK.START_TIME LIKE '{reservation_time}'")
        my_time_id = ""
        for b in times:
            my_time_id = b.time_id
        print("---------------------", my_time_id)
        with connection.cursor() as cursor:
            # the format looks like this: INSERT INTO RESERVATION VALUES(RESERVATION_ID, STUDENT_ID, ROOM_ID, RESERVATION_DATE, TIME_ID)
            #cursor.execute(f"INSERT INTO RESERVATION VALUES(RESERVATION_ID, {student_id}, {room_id}, '{reservation_date}', {time_id})")
            cursor.execute(f"INSERT INTO RESERVATION VALUES(RESERVATION_ID, {student_id}, {room_id}, '{reserved_day}', {my_time_id})")
            cursor.execute(f"DELETE FROM AVAILABILITY WHERE AVAILABILITY.ROOM_ID = {room_id} AND AVAILABILITY.TIME_ID = {my_time_id}")
            
    context = {
        'user_clicked_search': user_clicked_search,
        'rooms_found': rooms_found, 
        'time_searched': time_searched,
        'reservation_room': reservation_room,
        'reservation_time': reservation_time,
        'reserved_day': reserved_day
    }
    return render(request, 'finder/index.html', context)


def profile(request): 
    student_fname = ""
    student_lname = ""
    student_email = ""
    if "student_fname" in request.POST and "student_lname" in request.POST and "student_email" in request.POST:    
        student_fname = request.POST["student_fname"]
        student_lname = request.POST["student_lname"]
        student_email =  request.POST["student_email"]    
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO STUDENT VALUES(STUDENT_ID, '{student_fname}', '{student_lname}', '{student_email}')")
    context = {
        'student_fname': student_fname,
        'student_lname': student_lname,
        'student_email': student_email
    }
    return render(request, 'finder/profile.html', context)
