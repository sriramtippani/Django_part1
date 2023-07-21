from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class Information(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [BasicAuthentication, ]
#     permission_classes = [IsAuthenticated, ]



class Information(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]
