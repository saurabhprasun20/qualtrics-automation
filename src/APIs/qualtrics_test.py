from urllib import response
import requests

api_url = "https://reqres.in/api/users?page=2"
response = requests.get(api_url)
print(response.json())


