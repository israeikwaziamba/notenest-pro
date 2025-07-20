from django import forms
from .models import Course, CourseFile

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category']

class CourseFileForm(forms.ModelForm):
    class Meta:
        model = CourseFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }