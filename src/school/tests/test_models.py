from socket import SocketIO
from django.test import TestCase
from src.school.models import School

class TestSchoolModel(TestCase):
    def test_school_can_be_created(self):
        school = School.objects.create(name="testing2", max_capacity='5')

        school_result = School.objects.last()
        self.assertEqual(school_result.name , "testing2")