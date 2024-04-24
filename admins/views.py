from django.shortcuts import render, HttpResponse
from django.db.models import Avg, Max, Min
from .models import Professor, Department

# Create your views here.
def home(request):
    return HttpResponse("Administration Page")

from django.db.models import Avg, Max, Min
from .models import Professor, Department

def salary_report(request):
    departments = Department.objects.annotate(
        min_salary=Min('professor__salary'),
        max_salary=Max('professor__salary'),
        avg_salary=Avg('professor__salary')
    )
    return render(request, 'salary_report.html', {'departments': departments})