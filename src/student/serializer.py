from socket import SocketIO
from rest_framework import serializers
from src.student.models import Student
from src.school.models import School

class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'school']
    
    def create(self, validated_data):
        schoolId = validated_data.get('school', None)

        student =  Student.objects.filter(school=schoolId).count()
        print(f'student count {student} {schoolId}')

        school = School.objects.filter(id=schoolId).first()
        print(f'schoolLimit {school.max_capacity} {student}')
        if school.max_capacity != None and student <= school.max_capacity:
            print('creating....')
            student = Student.objects.create(first_name=validated_data.get('first_name', None), last_name=validated_data.get("last_name", None),school=school)
            if student:
                return student
