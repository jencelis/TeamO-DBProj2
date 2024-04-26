from django.shortcuts import render, HttpResponse
from django.db.models import Avg, Max, Min
from .models import Professor, Department, CourseSection, Funding, Publication
from .forms import PerformanceForm

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

def performance_request(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            # Here, you can process the data or redirect to another view
            return render(request, 'performance_results.html', {
                'form': form,
                'data': form.cleaned_data
            })
    else:
        form = PerformanceForm()
    return render(request, 'request_performance.html', {'form': form})

def professor_performance(request):
    # You might get these from the request, here hardcoding for simplicity
    professor_name = "John Doe"
    academic_year = "2023-2024"
    semester = "Fall"
    
    try:
        professor = Professor.objects.get(name=professor_name)
    except Professor.DoesNotExist:
        return HttpResponse("Professor not found", status=404)
    
    # Fetch course sections taught by the professor
    sections = CourseSection.objects.filter(professor=professor, academic_year=academic_year, semester=semester)
    total_students = sum(section.students.count() for section in sections)
    
    # Fetch total funding and publications
    total_funding = Funding.objects.filter(professor=professor, year=academic_year.split('-')[0]).aggregate(total=models.Sum('amount'))['total']
    total_publications = Publication.objects.filter(professor=professor, year_published__range=academic_year.split('-')).count()
    
    context = {
        'professor': professor,
        'sections_taught': len(sections),
        'total_students': total_students,
        'total_funding': total_funding,
        'total_publications': total_publications,
    }
    
    return render(request, 'professor_performance.html', context)
