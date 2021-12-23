import requests

import json

MERCHANT_ID = "5fd0928b1c849a7578ddf805"
MERCHANT_KEY = "JFc0Ee3mvD7Jji41Z0eieRODJKcye2AQy15m"

URL = 'https://checkout.paycom.uz/api'

def add_card(data):
    print(data)
    payload = {
        "id": 123,
        "method": "cards.create",
        "params": {
            "card": {
                "number": data['card_number'],
                "expire": data['card_expire']
            },
            "save": data['save_status']
        }
    }
    print(payload)
    headers = {"X-Auth": MERCHANT_ID}
    return requests.post(URL, data=json.dumps(payload), headers=headers)

def send_code(token):
    payload = {
        "id": 123,
        "method": "cards.get_verify_code",
        "params": {
            "token": token
        }
    }
    headers = {"X-Auth": MERCHANT_ID}
    return requests.post(URL, data=json.dumps(payload), headers=headers)

def verify_code(data):
    payload = {
        "id": 123,
        "method": "cards.verify",
        "params": {
            "token": data['token'],
            "code": data['code']
        }
    }
    headers = {"X-Auth": MERCHANT_ID}
    return requests.post(URL, data=json.dumps(payload), headers=headers)
