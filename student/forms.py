from django import forms
from student.models import Student

# Creates the form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"