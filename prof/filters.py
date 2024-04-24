import django_filters
from .models import *


class InstructorFilter(django_filters.FilterSet):
    class Meta:
        model = Instructor
        fields = {'name': ['icontains'],
                  'dept_name': ['exact'], }


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {'title': ['icontains']}