import json

from django.core.serializers import serialize
from django.http import HttpResponse

class FormSerialize(object):
    def serialize(self, emp):
        json_data = serialize('json', emp)
        py_dict = json.loads(json_data)
        final_list = []
        for x in py_dict:
            final_list.append(x['fields'])
        json_data = json.dumps(final_list)
        return json_data

class FormSer11(object):
    def m1(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)

