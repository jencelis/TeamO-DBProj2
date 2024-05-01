from django import forms
from .models import Instructor, Section


class PerformanceForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), empty_label=None)
    
    # Dynamic choices for academic_year and semester will be set in the __init__ method
    academic_year = forms.ChoiceField(choices=[])
    semester = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(PerformanceForm, self).__init__(*args, **kwargs)
        
        # Set choices for academic_year based on Section data
        academic_year_choices = Section.objects.order_by('year').values_list('year', flat=True).distinct()
        self.fields['academic_year'].choices = [(year, year) for year in academic_year_choices]
        
        # Set choices for semester based on Section data
        # Assuming that the 'semester' is stored as an integer that represents the term
        semester_choices = Section.objects.order_by('semester').values_list('semester', flat=True).distinct()
        self.fields['semester'].choices = [(semester, "Spring" if semester == 1 else "Fall" if semester == 2 else "Summer") for semester in semester_choices]
        
        # Updating the label function for the instructor field
        self.fields['instructor'].label_from_instance = lambda obj: f"{obj.name}"