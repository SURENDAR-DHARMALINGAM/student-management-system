from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializer


@login_required
def dashboard(request):
    search_query = request.GET.get('search', '').strip()

    students = Student.objects.all().order_by('-id')

    if search_query:
        students = students.filter(
            Q(student_name__icontains=search_query)
            | Q(roll_number__icontains=search_query)
        )

    context = {
        'students': students,
        'search_query': search_query,
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()

            messages.success(
                request,
                f'Student "{student.student_name}" added successfully.'
            )

            return redirect('dashboard')
    else:
        form = StudentForm()

    return render(
        request,
        'student_form.html',
        {
            'form': form,
            'page_title': 'Add Student',
            'button_text': 'Add Student',
        }
    )


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()

            messages.success(
                request,
                f'Student "{student.student_name}" updated successfully.'
            )

            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'student_form.html',
        {
            'form': form,
            'page_title': 'Edit Student',
            'button_text': 'Update Student',
        }
    )


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student_name = student.student_name
        student.delete()

        messages.success(
            request,
            f'Student "{student_name}" deleted successfully.'
        )

        return redirect('dashboard')

    return render(
        request,
        'student_confirm_delete.html',
        {
            'student': student,
        }
    )

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all().order_by('-id')

        search_query = self.request.query_params.get(
            'search',
            ''
        ).strip()

        if search_query:
            queryset = queryset.filter(
                Q(student_name__icontains=search_query)
                | Q(roll_number__icontains=search_query)
            )

        return queryset
