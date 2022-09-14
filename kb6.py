import requests
import json

from customers import *


for customer in customers:
    url = "http://125.212.225.71:8081/push_event/6"

    payload = json.dumps({
        "customer_email": customer.get('customer_email'),
        "customer_name": customer.get('customer_name'),
        "ma_khach_hang": customer.get('ma_khach_hang'),
        "customer_phone": "+84986651352",
        "event_id": "event_52",
        "access_token": "maitrongjthuaanf"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
