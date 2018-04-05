import requests

json = dict(result={'action': 'clientDemo', 'metadata': {'intentName': 'intenttt'}, 'parameters': 'params'})
response = requests.post('http://127.0.0.1:5000', json=json)
print(response)
