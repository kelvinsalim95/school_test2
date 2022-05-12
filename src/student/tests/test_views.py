from rest_framework.test import APITestCase
from src.school.models import School
from src.student.models import Student
from rest_framework import status

class TestSetup(APITestCase):
    url = '/students'

    def setUp(self):
        School.objects.create(name="testing", max_capacity='1')
        school = School.objects.last()
        Student.objects.create(first_name="testing", last_name="last", school=school)
        print(school.id)


    def test_get_student(self):
        response = self.client.get(self.url)
        result = response.json()
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["first_name"], 'testing')

    def test_create_student(self):
        data = {
            "first_name":"api_testing",
            "last_name":"last_testing",
            "school":5
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_max_capaity(self):
        response = ''
        data = {
            "first_name":"api_testing10",
            "last_name":"last_testing",
            "school":5
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        
