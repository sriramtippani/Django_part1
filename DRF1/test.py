import json
import time
import requests
BASE_URL = 'http://127.0.0.1:8000/DjangoRest/'
ENDPOINT = 'api/'

time.sleep(15)
print('get request')
def create_get(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    r = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
create_get(1)
time.sleep(15)
print('post request')

def create_post():
    data = {
        'eno': 107,
        'ename': 'kalalai',
        'esal': 44000,
        'eaddr': 'ooty',
    }
    r =requests.post(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
create_post()
time.sleep(15)
print('put request')

def create_put(id):
    data = {'id': id,
            'ename': 'pamiami',
            'esal': 45000,
            }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
create_put(6)
time.sleep(15)
print('delete request')

def create_delete(id):
    data = {'id': id}
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
create_delete(5)
