import io
import json

from app1.models import Employee
from app1.serializers import EmployeeSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

@method_decorator(csrf_exempt, name='dispatch')
class All_view_data(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            s1 = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(s1.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            qs = Employee.objects.all()
            s2 = EmployeeSerializer(qs, many=True)
            json_data = JSONRenderer().render(s2.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        s3 = EmployeeSerializer(data=py_data)
        if s3.is_valid():
            s3.save()
            msg = {'msg': 'Resource created successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(s3.errors)
            return HttpResponse(json_data, content_type='application/json', status=404)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        emp = Employee.objects.get(id=id)
        s4 = EmployeeSerializer(emp, data=py_data, partial=True)
        if s4.is_valid():
            s4.save()
            msg = {'msg': 'Resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(s4.errors)
            return HttpResponse(json_data, content_type='application/json', status=404)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'Resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')




