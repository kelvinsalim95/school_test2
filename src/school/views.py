from rest_framework import viewsets, response, status
from src.school.models import School
from src.school.serializer import SchoolSerializer
from rest_framework.permissions import AllowAny


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        resultset = School.objects.all()
        return resultset

