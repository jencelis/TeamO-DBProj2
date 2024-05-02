from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Avg, Max, Min, Sum, Count
from .models import Instructor, Department, Course, Funding, Publication, Teaches, Takes
from .forms import PerformanceForm

# Home page view
def admin_home(request):
    return render(request, 'admin_welcome.html')

def list_professors(request):
    sort_by = request.GET.get('sort', 'name') 


    if sort_by == 'name':
        professors = Instructor.objects.all().order_by('name')
    elif sort_by == 'dept':
        professors = Instructor.objects.all().order_by('dept_name_id')  
    elif sort_by == 'salary':
        professors = Instructor.objects.all().order_by('-salary')

    context = {
        'professors': professors,
        'current_sort': sort_by
    }
    return render(request, 'list_professors.html', context)

def salary_report(request):
    departments = Instructor.objects.exclude(dept_name__isnull=True).values('dept_name').annotate(
        min_salary=Min('salary'),
        max_salary=Max('salary'),
        avg_salary=Avg('salary')
    ).order_by('dept_name')  

    return render(request, 'salary_report.html', {'departments': departments})



def performance_report(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            instructor = form.cleaned_data['instructor']
            year = form.cleaned_data['academic_year']
            semester = form.cleaned_data['semester']

            teaches = Teaches.objects.filter(
                instructor=instructor, 
                year=year, 
                semester=semester
            ).values('course_id', 'section_id')
            course_section_student_counts = {}

            for pair in teaches:
                student_count = Takes.objects.filter(
                    section_id=pair['section_id'], 
                    course_id=pair['course_id']
                ).distinct().count()
                course_section_student_counts[(pair['course_id'], pair['section_id'])] = student_count
            total_students = sum(course_section_student_counts.values())
            total_funding = Funding.objects.filter(instructor=instructor, year=year).aggregate(total=Sum('amount'))['total'] or 0
            total_publications = Publication.objects.filter(instructor=instructor, year_published=year).count()

            
            course_count = teaches.aggregate(course_count=Count('course_id'))['course_count']
            context = {
                'instructor': instructor,
                'courses_taught': course_count,
                'total_students': total_students,
                'total_funding': total_funding,
                'total_publications': total_publications,
            }

            return render(request, 'performance_results.html', context)

    else:
        form = PerformanceForm()

    return render(request, 'request_performance.html', {'form': form})