from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Avg, Max, Min, Sum, Count
from .models import Instructor, Department, Course, Funding, Publication, Teaches, Takes
from .forms import PerformanceForm

# Home page view
def admin_home(request):
    return render(request, 'admin_welcome.html')

def list_professors(request):
    sort_by = request.GET.get('sort', 'name')  # Default sorting by name

    # Map 'sort' value to actual database fields
    if sort_by == 'name':
        professors = Instructor.objects.all().order_by('name')
    elif sort_by == 'dept':
        professors = Instructor.objects.all().order_by('dept_name_id')  # Sorting by foreign key reference
    elif sort_by == 'salary':
        professors = Instructor.objects.all().order_by('-salary')  # Descending order for salary

    context = {
        'professors': professors,
        'current_sort': sort_by
    }
    return render(request, 'list_professors.html', context)

# Salary report view for each department
def salary_report(request):
    # Aggregating salary data grouped by 'dept_name' directly in the Instructor model
    departments = Instructor.objects.exclude(dept_name__isnull=True).values('dept_name').annotate(
        min_salary=Min('salary'),
        max_salary=Max('salary'),
        avg_salary=Avg('salary')
    ).order_by('dept_name')  # Ensuring a consistent order

    return render(request, 'salary_report.html', {'departments': departments})



def performance_report(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            instructor = form.cleaned_data['instructor']
            year = form.cleaned_data['academic_year']
            semester = form.cleaned_data['semester']

            # Fetch teaches records filtered by instructor, year, and semester
            teaches = Teaches.objects.filter(instructor=instructor, year=year, semester=semester)
            course_sections_count = teaches.count()

            # Prepare a list of tuples for the composite key (course_id, sec_id, semester, year)
            section_keys = teaches.values_list('course_id', 'sec_id', 'semester', 'year')

            # Count total students by querying Takes with the composite keys
            total_students = Takes.objects.filter(
                section__course_id__in=[key[0] for key in section_keys],
                section__sec_id__in=[key[1] for key in section_keys],
                section__semester__in=[key[2] for key in section_keys],
                section__year__in=[key[3] for key in section_keys]
            ).distinct().count()

            # Fetch total funding and publications
            total_funding = Funding.objects.filter(instructor=instructor, year=year).aggregate(Sum('amount'))['amount__sum'] or 0
            total_publications = Publication.objects.filter(instructor=instructor, year_published=year).count()

            context = {
                'instructor': instructor.name,
                'courses_taught': course_sections_count,
                'total_students': total_students,
                'total_funding': total_funding,
                'total_publications': total_publications,
            }

            return render(request, 'performance_results.html', context)
        else:
            return render(request, 'request_performance.html', {'form': form})
    else:
        form = PerformanceForm()

    return render(request, 'request_performance.html', {'form': form})