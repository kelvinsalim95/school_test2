from sqlite3 import Time
from django.db import models
from src.utils.models import TimeTrackedModel


# Create your models here.

class School(TimeTrackedModel):
    name = models.CharField(max_length=20, unique=True)
    max_capacity = models.IntegerField()