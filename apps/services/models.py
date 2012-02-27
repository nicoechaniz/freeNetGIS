from django.db import models
from apps.services.constants import *

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=70)
    server = models.ForeignKey('devices.Server')
    type = models.CharField(max_length=4, choices=SERVICE_TYPE)
    status = models.CharField(max_length=2, choices=SERVICE_STATUS)