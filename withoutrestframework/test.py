import json

import requests
BASE_URL = 'http://127.0.0.1:8000/withoutrest/'
ENDPOINT = 'api/'

# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id': id
#         }
#     r = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# get_resource(30)

# def post_resource():
#     data = {
#             'eno': 106,
#             'ename': 'kariko',
#             'esal': 3000,
#             'eaddr': 'Kavatiol',
#     }
#     r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# post_resource()

# def put_resource(id):
#     data = {
#             'id': id,
#             'esal': 31000,
#     }
#     r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# put_resource(6)

def delete_resource(id):
    data = {
        'id': id,
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())
delete_resource(5)
