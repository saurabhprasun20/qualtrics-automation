import requests
import sys

sys.path.append('/Users/prasun/Desktop/PRODIGI/qualtrics-automation/src/Auth')
from bearer_token import getAuthKey

access_token = getAuthKey()
access_token = "Bearer "+access_token
header = {}
header["Content-Type"] = "application/json" #Don't use header = {"Authorization": "Bearer code"}.. doesnt work sometimes.
header["Authorization"]= access_token

def get_survey(survey_id):
    api_url= "https://fra1.qualtrics.com/API/v3/survey-definitions/"+survey_id
    response = requests.get(api_url , headers = header)
    return response

print(get_survey("SV_eEiCtQafwmW9doa").json())
