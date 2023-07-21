from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from app1.permissions import IsReadOnly, IsGETOrPatch, OurOwnPermissions


# Create your views here.
# class E1(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [IsAuthenticated, IsReadOnly, ]

# class E1(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [IsAuthenticated, IsGETOrPatch, ]

# class E1(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [OurOwnPermissions, ]

from rest_framework_simplejwt.authentication import JWTAuthentication


# class E1(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     authentication_classes = [JWTAuthentication, ]
#     permission_classes = [OurOwnPermissions, ]

class E1(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

