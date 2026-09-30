import requests

response = requests.Response()

response._content = b"this is not json"

response.json()