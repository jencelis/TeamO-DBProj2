import django.db.models.signals
from django.db.models import Count
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            instructor_name = form.cleaned_data['instructor']
            semester = form.cleaned_data['semester']

            instructor = get_object_or_404(Instructor, name=instructor_name)

            teachings = Teaches.objects.filter(
                teacher=instructor,
                semester__semester=semester
            )

            total_students = sum(teaching.course.students.count() for teaching in teachings)

            return render(request, 'indexResults.html', {'instructor': instructor,
                                                                            'teachings': teachings,
                                                                            'total_students': total_students})

    else:
        form = InstructorForm()

    return render(request, 'index.html', {'form': form})

def indexResults(request):

    instructor_name = request.POST.get('name')
    semester = request.POST.get('semester')
    instructor = Instructor.objects.get(name=instructor_name)

    courses = Course.objects.filter(instructor=instructor,semester=semester)
    total_students = sum(course.students.count() for course in courses)

    return render(request, 'indexResults.html', {'instructor': instructor,
                                                                    'courses_taught': len(courses),
                                                                    'total_students': total_students,})