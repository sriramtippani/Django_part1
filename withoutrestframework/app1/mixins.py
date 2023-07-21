import json

from django.http import HttpResponse
from django.core.serializers import serialize
import json

class StatusCodeMixin(object):
    def status_code_mixin(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)

class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json', qs)
        pdata = json.loads(json_data)
        result = []
        for obj in pdata:
            result.append(obj['fields'])
        json_data = json.dumps(result)
        return json_data
