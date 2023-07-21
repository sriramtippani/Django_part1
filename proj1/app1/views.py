# import json

# from django.core.serializers import serialize
import json

from django.http import HttpResponse
from django.shortcuts import render
from .forms import Job1Form
from .models import Job1Model
from django.views.generic import View
from .mixins import FormSerialize, FormSer11
from .utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
def home_page(request):
    return render(request, 'html/home.html')


def form_page(request):
    form = Job1Form()
    if request.method == 'POST':
        form = Job1Form(request.POST)
        if form.is_valid():
            form.save()
        return confirm_submit(request)
    return render(request, 'html/form.html', {'form': form})

def confirm_submit(request):
    return render(request, 'html/submit.html')

@method_decorator(csrf_exempt, name='dispatch')
class FormCRUDCBV(FormSerialize, FormSer11, View):
    def get(self, request, *args, **kwargs):
        # becouse get method you taken at test.py file (i.e., partner application) so, that's why we took here.
        emp = Job1Model.objects.all()

        # json_data = serialize('json', emp, fields=('First_Name', 'Last_Name'))
        # json_data = serialize('json', emp)
        # py_dict = json.loads(json_data)
        # final_list = []
        # for x in py_dict:
        #   final_list.append(x['fields'])
        # json_data = json.dumps(final_list)
        # The above comment for python login in mixins.py file for code reusability.

        json_data = self.serialize(emp)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, * args, ** kwargs):
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.m1(json_data, status=400)
        else:
            empdata = json.loads(data)
            form = Job1Form(empdata)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'resource created successfully'})
                return self.m1(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.m1(json_data, status=400)