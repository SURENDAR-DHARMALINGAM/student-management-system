from django.db import models


class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    mobile_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    date_of_admission = models.DateField()

    def __str__(self):
        return f"{self.roll_number} - {self.student_name}"