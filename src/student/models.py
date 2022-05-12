import uuid
from django.db import models
from src.utils.models import TimeTrackedModel
from src.school.models import School


# Create your models here.

class Student(TimeTrackedModel):
    student_id = models.UUIDField(max_length=20, default=uuid.uuid4)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(to=School, on_delete=models.DO_NOTHING, related_name="school_id", blank=False, null=False)