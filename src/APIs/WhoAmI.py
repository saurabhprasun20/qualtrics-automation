import requests
import base64

url = "https://fra1.qualtrics.com/oauth2/token"
username = "f0e28f65e885145e4764075008881a23"
password = "hnxtA89vzrzfI3yL2JBQ5rhFvBu6sfUvmIAhjIQnWk5bAGkKZqFBZ6lSwdFjE0Z0"
body = "grant_type=client_credentials&scope=manage:all"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
response = requests.post(url, auth=(username, password), data=body, headers= headers)
print(response.status_code)
print(response.json()["access_token"])

access_token = response.json()["access_token"]

access_token = "Bearer "+access_token

url2 = "https://fra1.qualtrics.com/API/v3/whoami"
header = {"Authorization": access_token}
response2 = requests.get(url=url2, headers=header)
print(response2.json())