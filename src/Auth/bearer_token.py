
import http.client
import mimetypes
import base64
import json,os
import requests
import time

#create the Base64 encoded basic authorization string
auth_key = ""
clientID="#Enter your clientId"
clientsecret="#Enter your secret key"
auth = "{0}:{1}".format(clientID, clientsecret)
encodedBytes=base64.b64encode(auth.encode("utf-8"))
authStr = str(encodedBytes, "utf-8")

def get_auth_key():
    #create the connection 
    conn = http.client.HTTPSConnection("fra1.qualtrics.com")
    body = "grant_type=client_credentials&scope=manage:all"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    headers['Authorization'] = 'Basic {0}'.format(authStr)

    #make the request
    conn.request("POST", "/oauth2/token", body, headers)
    res = conn.getresponse()
    data = res.read()
    key = json.loads(data.decode("utf-8"))
    return key["access_token"]


sibB = os.path.dirname(__file__)
def getAuthKey():
    with open(os.path.join(sibB,"auth.json"),"r+") as json_file:
        auth_file = json.load(json_file)
        if(auth_file['keyExists']==0):
            print("generating key")
            generated_key = get_auth_key()
            auth_file["keyExists"] = 1
            auth_file["key"] = generated_key
            json_file.seek(0)
            json.dump(auth_file,json_file)
            json_file.truncate()
            return generated_key
        elif(auth_file['keyExists']==1):
            print("Accessing stored key")
            stored_key = auth_file["key"]
            return stored_key




