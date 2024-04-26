from django import forms
from .models import Professor, CourseSection

class PerformanceForm(forms.Form):
    # Assuming you have a small set of professors and semesters predefined
    professor = forms.ModelChoiceField(queryset=Professor.objects.all(), empty_label=None)
    academic_year_choices = CourseSection.objects.order_by('academic_year').values_list('academic_year', flat=True).distinct()
    academic_year = forms.ChoiceField(choices=[(year, year) for year in academic_year_choices])
    semester_choices = [('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')]  # Predefined choices
    semester = forms.ChoiceField(choices=semester_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor'].label_from_instance = lambda obj: f"{obj.name}"