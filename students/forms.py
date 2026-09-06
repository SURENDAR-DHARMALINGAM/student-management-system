from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'roll_number',
            'student_name',
            'email',
            'mobile_number',
            'course',
            'year_of_study',
            'date_of_admission',
        ]

        widgets = {
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number',
            }),

            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',
            }),

            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number',
            }),

            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course',
            }),

            'year_of_study': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter year of study',
                'min': '1',
            }),

            'date_of_admission': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }