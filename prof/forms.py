from django import forms
from .models import Instructor, Section


class InstructorForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(), empty_label=None)
    semester = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(InstructorForm, self).__init__(*args, **kwargs)

        semester_choices = Section.objects.order_by('semester').values_list('semester', flat=True).distinct()
        self.fields['semester'].choices = [
            (semester, "Spring" if semester == 1 else "Fall" if semester == 2 else "Summer") for semester in
            semester_choices]

        self.fields['instructor'].label_from_instance = lambda obj: f"{obj.name}"