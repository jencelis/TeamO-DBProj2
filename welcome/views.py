from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import *
from .forms import *

# Create your views here.

def home(request):
    if request.method == 'POST':

        #button = request.POST.get('button_name')
        if request.POST.get('button_name') == 'adminButton':
            # re-direct to admin view
            return HttpResponseRedirect("/admins/")
        elif request.POST.get('button_name') == 'profButton':
            # re-direct to prof view
            return HttpResponseRedirect("/prof/")
        elif request.POST.get('button_name') == 'studButton':
            # re-direct to prof view
            return HttpResponseRedirect("/stud/")

            # create re-direct
    return render(request, 'welcomePage.html',{})