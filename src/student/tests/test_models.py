import sched
from socket import SocketIO
from django.test import TestCase
from src.student.models import Student
from src.school.models import School

class TestStudentModel(TestCase):
    def setUP(self):
        school = School.objects.create(name="testing3", max_capacity='5')
        return School.objects.last()
    def test_student_can_be_created(self):
        school = self.setUP()
 
        student = Student.objects.create(first_name="testing", last_name="last", school=school)

        student_result = Student.objects.last()
        self.assertEqual(student_result.first_name , "testing")