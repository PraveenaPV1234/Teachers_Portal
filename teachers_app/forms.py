from django import forms
from .models import Student, Subjects_Mark

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class SubjectsMarkForm(forms.ModelForm):
    class Meta:
        model = Subjects_Mark
        fields = ['subject', 'mark']