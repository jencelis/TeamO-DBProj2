from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
import hashlib

from .models import *
from .forms import *

# Function to hash strings using SHA-256
def hash_string(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

# Create your views here.

def home(request):
    if request.method == 'POST':

        username = request.POST.get('adminName')
        password = request.POST.get('adminPsswrd')

        #button = request.POST.get('button_name')
        if request.POST.get('button_type') == 'adminButton':
            # Query the database to check if the provided username and password match
            user = User.objects.filter(username=hash_string(username), password=hash_string(password)).first()

            if user:
                # re-direct to admin view
                return HttpResponseRedirect("/admins/")
        elif request.POST.get('button_type') == 'profButton':
            # re-direct to prof view
            return HttpResponseRedirect("/prof/")
        elif request.POST.get('button_type') == 'studButton':
            # re-direct to prof view
            return HttpResponseRedirect("/stud/")

            # create re-direct
    return render(request, 'welcomePage.html',{})
