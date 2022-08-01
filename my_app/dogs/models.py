from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.
class Dog(ExportModelOperationsMixin("dog"), models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    likes_to_bark = models.BooleanField()
    is_test = models.BooleanField(default=False)