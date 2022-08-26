import requests
import json
import sys

sys.path.append('/Users/prasun/Desktop/PRODIGI/qualtrics-automation/src/Auth')
from bearer_token import getAuthKey

api_url = "https://fra1.qualtrics.com/API/v3/survey-definitions"
access_token = getAuthKey()
access_token = "Bearer "+access_token
# header =  {"Content-Type":"application/json"}
header = {}
header["Content-Type"] = "application/json" #Don't use header = {"Authorization": "Bearer code"}.. doesnt work sometimes.
header["Authorization"]= access_token
print(access_token)

data = {
  'SurveyName': 'Automated Test Survey 1',
  'Language': 'EN',
  'ProjectCategory': 'CORE'
}

def set_survey(data):
  api_url = "https://fra1.qualtrics.com/API/v3/survey-definitions"
  response = requests.post(api_url, data=json.dumps(data),headers=header)
  return response

# print(set_survey(data).json())