import django.db.models.signals
from django.shortcuts import render, HttpResponse
from .models import Instructor
# Create your views here.

'''
def listProfView(request):
    data = Instructor.objects.all()
    context = {"Instructors": data}
    return render(request, 'listprofs.html',context)
'''

def BootstrapFilterView(request):
    profName = request.GET.get('profName')
    print(profName)
    return render(request, 'bootstrap_form.html',{})
