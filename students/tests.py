from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Student


User = get_user_model()


class StudentAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPassword123'
        )

        # Authenticate the API client
        self.client.force_authenticate(user=self.user)

        # Create sample students
        self.student = Student.objects.create(
            roll_number='TEST001',
            student_name='Test Student',
            email='test@example.com',
            mobile_number='9876543210',
            course='Python Full Stack',
            year_of_study=1,
            date_of_admission=date(2026, 9, 6)
        )

    def test_student_list(self):
        """Test GET all students."""
        url = reverse('student-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_detail(self):
        """Test GET one student."""
        url = reverse(
            'student-detail',
            kwargs={'pk': self.student.id}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['roll_number'],
            'TEST001'
        )

    def test_create_student(self):
        """Test POST creates a student."""
        url = reverse('student-list')

        data = {
            'roll_number': 'TEST002',
            'student_name': 'New Student',
            'email': 'newstudent@example.com',
            'mobile_number': '9123456789',
            'course': 'Django Full Stack',
            'year_of_study': 2,
            'date_of_admission': '2026-09-06'
        }

        response = self.client.post(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Student.objects.filter(
                roll_number='TEST002'
            ).exists()
        )

    def test_update_student(self):
        """Test PUT updates a student."""
        url = reverse(
            'student-detail',
            kwargs={'pk': self.student.id}
        )

        data = {
            'roll_number': 'TEST001',
            'student_name': 'Updated Student',
            'email': 'updated@example.com',
            'mobile_number': '9876543210',
            'course': 'Django Full Stack',
            'year_of_study': 2,
            'date_of_admission': '2026-09-06'
        }

        response = self.client.put(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.student.refresh_from_db()

        self.assertEqual(
            self.student.student_name,
            'Updated Student'
        )

    def test_partial_update_student(self):
        """Test PATCH updates only selected fields."""
        url = reverse(
            'student-detail',
            kwargs={'pk': self.student.id}
        )

        data = {
            'student_name': 'Patched Student'
        }

        response = self.client.patch(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.student.refresh_from_db()

        self.assertEqual(
            self.student.student_name,
            'Patched Student'
        )

    def test_delete_student(self):
        """Test DELETE removes a student."""
        url = reverse(
            'student-detail',
            kwargs={'pk': self.student.id}
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Student.objects.filter(
                id=self.student.id
            ).exists()
        )

    def test_search_student(self):
        """Test searching by student name."""
        url = reverse('student-list')

        response = self.client.get(
            url,
            {'search': 'Test Student'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(
            any(
                student['roll_number'] == 'TEST001'
                for student in response.data['results']
            )
        )

    def test_duplicate_roll_number(self):
        """Test duplicate roll number is rejected."""
        url = reverse('student-list')

        data = {
            'roll_number': 'TEST001',
            'student_name': 'Another Student',
            'email': 'another@example.com',
            'mobile_number': '9123456789',
            'course': 'Python',
            'year_of_study': 1,
            'date_of_admission': '2026-09-06'
        }

        response = self.client.post(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_mobile_number(self):
        """Test invalid mobile number is rejected."""
        url = reverse('student-list')

        data = {
            'roll_number': 'TEST003',
            'student_name': 'Invalid Mobile',
            'email': 'invalidmobile@example.com',
            'mobile_number': '12345',
            'course': 'Python',
            'year_of_study': 1,
            'date_of_admission': '2026-09-06'
        }

        response = self.client.post(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_year(self):
        """Test invalid year of study is rejected."""
        url = reverse('student-list')

        data = {
            'roll_number': 'TEST004',
            'student_name': 'Invalid Year',
            'email': 'invalidyear@example.com',
            'mobile_number': '9123456789',
            'course': 'Python',
            'year_of_study': 10,
            'date_of_admission': '2026-09-06'
        }

        response = self.client.post(
            url,
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_nonexistent_student(self):
        """Test requesting a student that does not exist."""
        url = reverse(
            'student-detail',
            kwargs={'pk': 99999}
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )