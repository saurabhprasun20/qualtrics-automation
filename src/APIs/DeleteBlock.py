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


def delete_block(survey_id, block_id):
    api_url = "https://fra1.qualtrics.com/API/v3/survey-definitions/{0}/blocks/{1}".format(survey_id,block_id)
    print(api_url)
    response = requests.delete(api_url,headers=header)
    return response

# survey_id = "SV_1RMQQpcjjZgoQTA"
# block_id = "BL_0rLlsl91f7V5c0K"
# print(type(survey_id))
# print(type(block_id))
# resp = delete_block(survey_id,block_id).json()
# print(resp)
