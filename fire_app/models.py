
from django.db import models

class ForestData(models.Model):
    temperature = models.IntegerField()
    oxygen = models.IntegerField()
    humidity = models.IntegerField()
