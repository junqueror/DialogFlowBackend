import requests

CLIENT_ACCESS_TOKEN = "c87709891561448daca17fda76f1e491"

url = "https://api.api.ai/v1/query"
headers = {"Authorization": "Bearer {0}".format(CLIENT_ACCESS_TOKEN),
           'Content-Type': 'application/json; charset\\u003dutf-8.'}
data = {"event": {
    "name": "pushNotification",
    "data": {}
},
    "timezone": "Europe/Paris",
    "lang": "es",
    "sessionId": "ba79ff79-0c67-b329-6b2e-733e6cf4b74c",
    "version":20180508
}

response = requests.post(url=url, headers=headers, json=data)

print(response)
