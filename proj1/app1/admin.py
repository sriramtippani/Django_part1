from django.contrib import admin
from app1.models import Job1Model

# Register your models here.
class Job1Admin(admin.ModelAdmin):
    list_display = ['id', 'First_Name', 'Last_Name', 'Age', 'Gender', 'Phone_Number', 'Email_Address', 'Address', 'Date_Of_Birth', 'date', 'time']

admin.site.register(Job1Model, Job1Admin)