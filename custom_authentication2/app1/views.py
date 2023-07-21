from django.shortcuts import render
from app1.authentications import M1
from rest_framework.viewsets import ModelViewSet
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [M1, ]
    permission_classes = [IsAuthenticated, ]
