import requests
import json

from customers import *


for customer in customers:
    url = "http://125.212.225.71:8081/push_event/1"

    payload = json.dumps({
        "customer_email": customer.get('customer_email'),
        "customer_name": customer.get('customer_name'),
        "ma_khach_hang": customer.get('ma_khach_hang'),
        "customer_phone": "0986651553",
        "event_id": "event_51",
        "contract_id": customer.get('contract_id'),
        "access_token": "maitrongjthuaanf"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
