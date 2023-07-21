from django.utils import timezone

from django.db import models
from datetime import datetime
x = datetime.now()
y = x.strftime('%d-%m-%Y')

# Create your models here.
from django.utils.datetime_safe import datetime


class Job1Model(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=7)
    Phone_Number = models.PositiveBigIntegerField()
    Email_Address = models.EmailField()
    Address = models.TextField(max_length=80)
    Date_Of_Birth = models.DateField('DOB: (yyyy/mm/dd)', auto_now_add=False, auto_now=False, blank=True, null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)