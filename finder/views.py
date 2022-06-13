from django.shortcuts import render
# from .forms import NameForm
from .models import STUDENT, ROOM, STUDENT_ROOM
from django.template import loader
from django.http import HttpResponse

# def index(request):
#     return render(request, 'finder/index.html') 

def index(request):
    rooms = [ "Rice Hall " + str(i) for i in range(120, 140) ]
    return render(request, 'finder/index.html', {'rooms': rooms})

def testing(request):
    my_data = STUDENT.objects.all()
    template = loader.get_template('index.html')
    context = { 'students': my_data }
    return HttpResponse(template.render(context, request))
    