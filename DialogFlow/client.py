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
    "sessionId": "d0d075a2-d330-4eea-b6a9-6f891b468290",
    "version":20180508
}

response = requests.post(url=url, headers=headers, json=data)

print(response)
