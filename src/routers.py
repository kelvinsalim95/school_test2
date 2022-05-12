from re import S
from rest_framework_nested import routers
from src.school.views import SchoolViewSet
from src.student.views import StudentViewSet
from django.urls import path, include


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'schools', viewset=SchoolViewSet, basename ='schools')

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
school_router.register(r'students', StudentViewSet, basename='maildrops')

router.register(r'students', viewset=StudentViewSet, basename ='students')

urlpatterns =[
    path('' , include(router.urls)),
    path('' , include(school_router.urls))
]
