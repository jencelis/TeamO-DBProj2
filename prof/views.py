import django.db.models.signals
from django.shortcuts import render, HttpResponse
from .models import Instructor
# Create your views here.

'''
def home(request):
    return HttpResponse("Professor page")
'''


def home(request):
    profs = Instructor.objects.all()
    return render(request, 'prof/index.html',{'Professors':profs})