# Import the models
from .models import Course, Section
from django.shortcuts import render


# Update the view
def home(request):
    # Get distinct department names
    departments = Course.objects.values_list('dept_name', flat=True).distinct()

    # Get distinct years
    years = Section.objects.values_list('year', flat=True).distinct()

    # Get distinct semesters
    semesters = Section.objects.values_list('semester', flat=True).distinct()

    if request.method == 'POST':
        department = request.POST.get('department')
        year = request.POST.get('year')
        semester = request.POST.get('semester')

        # Query the course sections based on the selected department, year, and semester
        course_sections = Section.objects.filter(course__dept_name=department, year=year, semester=semester)

        print(course_sections)

        return render(request, 'home.html', {'departments': departments, 'years': years, 'semesters': semesters, 'course_sections': course_sections})
    else:
        # Render the empty form with selectable options
        return render(request, 'home.html', {'departments': departments, 'years': years, 'semesters': semesters})
