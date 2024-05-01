from django import forms
from .models import Instructor, Section, Teaches

class PerformanceForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), empty_label="Select Instructor")
    academic_year = forms.ModelChoiceField(queryset=Teaches.objects.order_by('year').values_list('year', flat=True).distinct(), empty_label="Select Year")
    semester = forms.ModelChoiceField(queryset=Teaches.objects.order_by('semester').values_list('semester', flat=True).distinct(), empty_label="Select Semester")

    def __init__(self, *args, **kwargs):
        super(PerformanceForm, self).__init__(*args, **kwargs)
        # Optionally add field help texts
        self.fields['instructor'].help_text = "Select an instructor from the list."
        self.fields['academic_year'].help_text = "Select the academic year."
        self.fields['semester'].help_text = "Select the semester term."
        # Label for Instructor Field to display names
        self.fields['instructor'].label_from_instance = lambda obj: f"{obj.name}"