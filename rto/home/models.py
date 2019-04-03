from django.db import models

class Record(models.Model):
    current = models.CharField(max_length=6)
    place = models.CharField(max_length=100)
    zone = models.CharField(max_length=25)