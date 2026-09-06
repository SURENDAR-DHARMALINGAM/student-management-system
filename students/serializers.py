from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'id',
            'roll_number',
            'student_name',
            'email',
            'mobile_number',
            'course',
            'year_of_study',
            'date_of_admission',
        ]

    def validate_roll_number(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Roll number cannot be empty."
            )

        return value

    def validate_student_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Student name cannot be empty."
            )

        if len(value) < 2:
            raise serializers.ValidationError(
                "Student name must contain at least 2 characters."
            )

        return value

    def validate_mobile_number(self, value):
        value = value.strip()

        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Mobile number must contain exactly 10 digits."
            )

        return value

    def validate_year_of_study(self, value):
        if value < 1 or value > 6:
            raise serializers.ValidationError(
                "Year of study must be between 1 and 6."
            )

        return value