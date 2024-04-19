import django.db.models.signals
from django.shortcuts import render, HttpResponse

from .models import Instructor



# Create your views here.


def listProfView(request):
    data = Instructor.objects.all()
    context = {"Instructors": data}
    return render(request, 'listprofs.html',context)


def testing(request):
    data = Instructor.objects.all()
    context = {"Instructors": data}
    return render(request, 'testing.html',context)

'''
def BootstrapFilterView(request):
  # names = models.Instructor.objects.all()
 #  teach = models.Teaches.objects.all()

   profName = request.GET.get('profName')
   profTeaches = request.GET.get('profTeaches')
   context = {
  #    'queryset': names + "" + teach
   }
   return render(request, 'bootstrap_form.html',{})
'''

def BootstrapFilterView(request):
    names = Instructor.objects.all()
    context = {"Instructors": names}
    return render(request, 'bootstrap_form.html',context)