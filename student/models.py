from operator import mod
from django.db import models
from uuid import uuid4


class Student(models.Model):
    id = models.AutoField(primary_key=True, default=uuid4)
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
