from django.db import models

# Create your models here.
class SriModel(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.TextField(max_length=64)