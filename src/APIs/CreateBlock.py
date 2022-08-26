import requests
import json
import sys

sys.path.append('/Users/prasun/Desktop/PRODIGI/qualtrics-automation/src/Auth')
from bearer_token import getAuthKey

access_token = getAuthKey()
access_token = "Bearer "+access_token
# header =  {"Content-Type":"application/json"}
header = {}
header["Content-Type"] = "application/json" #Don't use header = {"Authorization": "Bearer code"}.. doesnt work sometimes.
header["Authorization"]= access_token
print(access_token)

data = {
    "Description": "Test Block"
}

def create_block(survey_id,data):
    api_url = "https://fra1.qualtrics.com/API/v3/survey-definitions/{0}/blocks".format(survey_id)
    response = requests.post(api_url,data=json.dumps(data),headers=header)
    return response

# print(create_block("SV_eEiCtQafwmW9doa",data).json())
