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
    "ChoiceOrder":[
        "1",
        "2",
        "3"
    ],
    "Choices":{
        "1":{
            "Display":"Choice no 1 is this"
        },
        "2":{
            "Display":"Choice no 2 is that"
        },
        "3":{
            "Display":"Choice no 3 is what"
        }
    },
    "Configuration":{
        "QuestionDescriptionOption": "UseText"
    },
    "Language":[
    ],
    "NextChoiceId": 4,
    "NextAnswerId": 1,
    "QuestionID": "Q4",
    "QuestionDescription":"This is my second block test question",
    "QuestionText":"This is my second block test question <div><br></div>",
    "QuestionType":"MC",
    "Selector":"SAVR",
    "SubSelector":"TX",
    "Validation":
        {
            "Settings":
            {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None"
            }
        }
    
    
}

def set_question(survey_id,block_id,data):
    api_url = "https://fra1.qualtrics.com/API/v3/survey-definitions/{0}/questions".format(survey_id)
    if(block_id is not None):
        api_url = api_url+"?blockId="+block_id
    response = requests.post(api_url,data=json.dumps(data),headers=header)
    return response

# print(set_question("SV_eEiCtQafwmW9doa", "BL_3lzQWlJlwNCWaBo",data).json())
