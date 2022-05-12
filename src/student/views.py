from rest_framework import viewsets, response, status
from src.student.models import Student
from src.school.models import School
from src.student.serializer import StudentSerializer
from rest_framework.permissions import AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        if self.kwargs == {}:
            return Student.objects.all()
        return Student.objects.filter(school=self.kwargs['schools_pk'])


    def create(self , request, **kwargs):
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = serializer.create(validated_data=serializer.data)
            return response.Response({'status_code': 201, 'data': request.data}, status=status.HTTP_201_CREATED)