from django.shortcuts import render
# from .forms import NameForm
from .models import Room


# def index(request):
#     return render(request, 'finder/index.html') 

def index(request):
    rooms = [ "Rice Hall " + str(i) for i in range(120, 140) ]
    return render(request, 'finder/index.html', {'rooms': rooms})

    