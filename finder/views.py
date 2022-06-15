from django.shortcuts import render
from .forms import DweetForm
from .models import Student, Room
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# def index(request):
#     return render(request, 'finder/index.html') 

def index(request):
    user_clicked_search = False
    data = ""
    time_searched = ""
    if request.method == "POST":
        #user_clicked_search = True
        time_searched = request.POST["time_searched"]
        data = Room.objects.raw(
            f"""
            SELECT 
                TIME_BLOCK.TIME_ID,
                TIME_BLOCK.START_TIME,
                AVAILROOM.AVAILABILITY_ID,
                AVAILROOM.ROOM_ID,
                AVAILROOM.ROOM_NUMBER
            FROM
                TIME_BLOCK
            INNER JOIN
                (SELECT 
                    AVAILABILITY.TIME_ID,
                    AVAILABILITY.AVAILABILITY_ID,
                    ROOM.ROOM_ID,
                    ROOM.ROOM_NUMBER
                FROM
                    AVAILABILITY
                INNER JOIN ROOM
                WHERE AVAILABILITY.ROOM_ID = ROOM.ROOM_ID) AS AVAILROOM ON TIME_BLOCK.TIME_ID = AVAILROOM.TIME_ID
            WHERE TIME_BLOCK.TIME_ID = '{time_searched}';
            """
        )

    context = { 'user_clicked_search': user_clicked_search, 'data': data, 'time_searched': time_searched }
    return render(request, 'finder/index.html', context)