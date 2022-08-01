from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Cat(ExportModelOperationsMixin("cat"), models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    likes_to_drop_things = models.BooleanField()
    is_test = models.BooleanField(default=False)