import json
from django.shortcuts import render
from django.views.generic import View
from .utils import is_json
from .mixins import StatusCodeMixin, SerializeMixin
from .models import SriModel
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import SriForm

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class All_information_without_rest(View, StatusCodeMixin, SerializeMixin):

    def get_object_by_id(self, id):
        try:
            emp = SriModel.objects.get(id=id)
        except SriModel.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data'})
            return self.status_code_mixin(json_data, status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                json_data = json.dumps({'msg': 'The required resource is not available with matched id'})
                return self.status_code_mixin(json_data, status=404)
            json_data = self.serialize([std, ])
            return self.status_code_mixin(json_data)
        qs = SriModel.objects.all()
        json_data = self.serialize(qs)
        return self.status_code_mixin(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data'})
            return self.status_code_mixin(json_data, status=400)
        else:
            pdata = json.loads(data)
            form = SriForm(pdata)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'Resource created successfully'})
                return self.status_code_mixin(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.status_code_mixin(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data'})
            return self.status_code_mixin(json_data, status=400)
        else:
            pdata = json.loads(data)
            id = pdata.get('id', None)
            if id is None:
                json_data = json.dumps({'msg': 'To perform updation id is mandatory, please provide valid id'})
                return self.status_code_mixin(json_data, status=404)
            else:
                std = self.get_object_by_id(id)
                if std is None:
                    json_data = json.dumps({'msg': 'The required resource is not available with matched id'})
                    return self.status_code_mixin(json_data, status=404)
                else:
                    provided_data = json.loads(data)
                    original_data = {
                                    'eno': std.eno,
                                    'ename': std.ename,
                                    'esal': std.esal,
                                    'eaddr': std.eaddr,
                                    }
                    original_data.update(provided_data)
                    form = SriForm(original_data, instance=std)
                    if form.is_valid():
                        form.save(commit=True)
                        json_data = json.dumps({'msg': 'Resource created successfully'})
                        return self.status_code_mixin(json_data)
                    if form.errors:
                        json_data = json.dumps(form.errors)
                        return self.status_code_mixin(json_data, status=404)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data'})
            return self.status_code_mixin(json_data, status=400)
        else:
            pdata = json.loads(data)
            id = pdata.get('id', None)
            if id is None:
                json_data = json.dumps({'msg': 'To perform deletion id is mandatory, please provide valid id'})
                return self.status_code_mixin(json_data, status=404)
            else:
                std = self.get_object_by_id(id)
                if std is None:
                    json_data = json.dumps({'msg': 'The required resource is not available with matched id'})
                    return self.status_code_mixin(json_data, status=404)
                else:
                    del_in = std.delete()
                    json_data = json.dumps({'msg': 'successfully deleted'})
                    return self.status_code_mixin(json_data)
















