from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app1.models import Employee
from app1.serializers import EmployeeSerializer

# Create your views here.
class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
