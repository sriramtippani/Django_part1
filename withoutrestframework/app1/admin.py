from django.contrib import admin
from app1.models import SriModel

# Register your models here.
class SriAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

admin.site.register(SriModel, SriAdmin)