from django.shortcuts import render, HttpResponse
from django.db.models import Avg, Max, Min, Sum, Count
from .models import Instructor, Department, Course, Funding, Publication
from .forms import PerformanceForm

# Home page view
def admin_home(request):
    return HttpResponse("Administration Page")

# Salary report view for each department
def salary_report(request):
    # Aggregating salary data grouped by 'dept_name' directly in the Instructor model
    departments = Instructor.objects.values('dept_name').annotate(
        min_salary=Min('salary'),
        max_salary=Max('salary'),
        avg_salary=Avg('salary')
    ).order_by('dept_name')  # Ensuring a consistent order

    return render(request, 'salary_report.html', {'departments': departments})

def performance_request(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            instructor_name = form.cleaned_data['instructor']
            academic_year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']

            # Fetch the instructor based on the name
            instructor = get_object_or_404(Instructor, name=instructor_name)

            # Fetch the teaching records from Teaches model
            teachings = Teaches.objects.filter(
                teacher=instructor,
                year__year=academic_year,
                semester__semester=semester
            )

            # Assuming you have a students field in the Section model
            total_students = sum(teaching.course.students.count() for teaching in teachings)

            # Your logic to fetch total funding and publications goes here
            # ...

            # Prepare the context
            context = {
                'instructor': instructor,
                'teachings': teachings,
                'total_students': total_students,
                # Add additional context for funding and publications
            }

            return render(request, 'performance_results.html', context)

    else:
        form = PerformanceForm()

    return render(request, 'request_performance.html', {'form': form})

# Detailed performance data for a specific instructor
def instructor_performance(request):
    # For simplicity, using hardcoded values, but these should ideally come from the request or form
    instructor_name = "John Doe"
    academic_year = "2023-2024"
    semester = "Fall"
    
    try:
        instructor = Instructor.objects.get(name=instructor_name)
    except Instructor.DoesNotExist:
        return HttpResponse("Instructor not found", status=404)
    
    # Fetch courses taught by the instructor
    courses = Course.objects.filter(instructor=instructor, academic_year=academic_year, semester=semester)
    total_students = sum(course.students.count() for course in courses)
    
    # Fetch total funding and publications
    total_funding = Funding.objects.filter(instructor=instructor, year=academic_year.split('-')[0]).aggregate(total=Sum('amount'))['total']
    total_publications = Publication.objects.filter(instructor=instructor, year_published__range=academic_year.split('-')).count()
    
    context = {
        'instructor': instructor,
        'courses_taught': len(courses),
        'total_students': total_students,
        'total_funding': total_funding,
        'total_publications': total_publications,
    }
    
    return render(request, 'instructor_performance.html', context)