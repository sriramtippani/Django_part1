import json

import requests
BASE_URL = 'http://127.0.0.1:8000/job/'
ENDPOINT = 'apiresult/'
def get_response():
    req = requests.get(BASE_URL + ENDPOINT)
    if req.status_code in range(200, 300):
        data = req.json()
        print(req.status_code)
        print(data)
    else:
        print('something went wrong.')
        print('status code: ', req.status_code)
get_response()

def create_resource():
    new_emp = {
        "First_Name": "sri sri",
        "Last_Name": "tipi naiia",
        "Age": 22,
        "Gender": "m",
        "Phone_Number": 8125367890,
        "Email_Address": "srisritipinaiia2000@gmail.com",
        "Address": "Barampur",
        "Date_Of_Birth": "2022-08-10"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())

create_resource()