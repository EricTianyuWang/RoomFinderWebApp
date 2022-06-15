from django.shortcuts import render
# from .forms import NameForm
from .models import Student
from django.template import loader
from django.http import HttpResponse

# def index(request):
#     return render(request, 'finder/index.html') 

def index(request):
    students = Student.objects.all()
    context = { 'students': students }
    return render(request, 'finder/index.html', context)
