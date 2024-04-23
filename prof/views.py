import django.db.models.signals
from django.shortcuts import render, HttpResponse
from .models import *
from .filters import *

# Create your views here.

def BootstrapFilterView(request):

    return render(request, 'bootstrap_form.html',{})




def index(request):
    prof_filter = InstructorFilter(request.GET, queryset=Instructor.objects.all())

    context = {
        'form': prof_filter.form,
        'profs': prof_filter.qs
    }
    return render(request, 'index.html',context)

'''
def courseIndex(request):
'''