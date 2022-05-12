from rest_framework.test import APITestCase
from src.school.models import School
from src.student.models import Student


class TestSetup(APITestCase):
    url = '/schools'

    def setUp(self):
        School.objects.create(name="testing10", max_capacity='1')
        school = School.objects.last()
        Student.objects.create(first_name="testing", last_name="last", school=school)
        return school

    def test_get_school(self):
        response = self.client.get(self.url)
        result = response.json()
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], 'testing10')
    
    def test_get_student_from_school(self):
        url = f'/schools/2/students'
        print(url)
        response = self.client.get(url)
        result = response.json()
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(result, list)
        
