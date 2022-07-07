from django.db import models
from uuid import uuid4


class Car(models.Model):
    id = models.AutoField(primary_key=True, default=uuid4)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year_of_manufacturing = models.DateField(null=True)
