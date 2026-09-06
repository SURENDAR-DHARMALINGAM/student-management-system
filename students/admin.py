from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_number',
        'student_name',
        'email',
        'mobile_number',
        'course',
        'year_of_study',
        'date_of_admission',
    )

    search_fields = (
        'roll_number',
        'student_name',
        'email',
    )

    list_filter = (
        'course',
        'year_of_study',
    )