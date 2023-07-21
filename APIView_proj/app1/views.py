from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.



# class EmployeeListAPIView(APIView):
#     def get(self,request, *args, **kwargs):
#         colors = ['Red', 'Yellow', 'Green', 'Blue']
#         return Response({'msg': 'happy pongal', 'colors': colors})

# class EmployeeListAPIView(APIView):
#     def get(self, request, format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs, many=True)
#         return Response(serializer.data)

# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs

# class EmployeeListAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeListAPIView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

class E1(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class E2(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer