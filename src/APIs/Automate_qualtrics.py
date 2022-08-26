import os
from CreateSurvey import set_survey
from CreateBlock import create_block
from CreateQuestion import set_question
from DeleteBlock import delete_block
import csv, json

survey_name = ""
file_name = ""

print("Loading survey data")
json_file = open('../data/survey.json')
survey_data = json.load(json_file)
print(survey_data)

# print("Opening the file to read and create new survey")
file_dir = os.path.dirname(os.path.realpath(__file__))
print(file_dir)
full_path =  file_dir.replace('APIs', 'data')
os.chdir(full_path)
print(full_path)

for filename in os.listdir(full_path):
    if (filename=="citizen_science_survey.csv"):
        file_name = filename
        survey_name = filename.split('.')[0]
        survey_data['SurveyName'] = survey_name
    
# print(survey_data)
# print("Creating survey with above data")
# print("Reading below file to create survey")
print(file_name)
survey_response = set_survey(survey_data).json()
# print("survey created and the response is ")
print(survey_response)
survey_id = survey_response["result"]["SurveyID"]
print("Survey id of the created survey is "+survey_id)
default_block_id=survey_response["result"]["DefaultBlockID"]
# print("Default block id is "+default_block_id)
# print("Deleting default block before putting new questions and blocks")
delete_block_response = delete_block(survey_id, default_block_id)
print("Response after deleteing the default block")
print(delete_block_response)
# print(full_path+"/"+file_name)

# print("Loading question json file to create the questions")
json_file = open('../data/question_1.json')
question_json1 = json.load(json_file)
# print(question_json1)


# print("Loading question json file to create the questions")
json_file = open('../data/question.json')
question_json = json.load(json_file)
# print(question_json)

# print("Loading question json file to create the hate speech questions")
json_file = open('../data/question.json')
hate_speech_json = json.load(json_file)
# print(hate_speech_json)

# print("Loading question json file to create the questions")
json_file = open('../data/question_hs.json')
hate_speech_json_2 = json.load(json_file)
# print(hate_speech_json_2)

# print("Loading block json file to create block")
json_file = open('../data/block.json')
block_json = json.load(json_file)
# print(block_json)

hate_speech_file = "hate_speech_question.csv"
hate_speech_file_2 = "hate_speech_question_2.csv"

js_script = "Qualtrics.SurveyEngine.addOnload(function()\n{\n\t/*Place your JavaScript here to run when the page loads*/\n\tjQuery(\"#button\").click(function() {\n    \tjQuery(\"#infodiv\").toggle();\n\t\t\n\t\tvar elem = document.getElementById(\"button\");\n\t\tconsole.log(\"elem is \"+elem);\n\t\tconsole.log(\"elem value is \"+elem.innerHTML);\n        if (elem.innerHTML==\"Click to read full article\") elem.innerHTML = \"Collapse the article\";\n        else elem.innerHTML = \"Click to read full article\";\n\n\t}\n\t);\n\t\n\tconsole.log(\"question id is :\"+this.questionId);\n\tconsole.log(\"blockid is:\"+ this.blockId);\n\tconst no_id = this.questionId.substring(3);\n\tprev_question = this.questionId;\n\tif(!arr1.includes(this.questionId)){\n\t\tjQuery(\"#\"+this.questionId).hide();\n\t\tif(no_id % 3 != 0){\n\t\t\tthis.clickNextButton();\n\t\t}\n\t}\n\n\n});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});"
js_script_hs = "Qualtrics.SurveyEngine.addOnload(function()\n{\n\t/*Place your JavaScript here to run when the page loads*/\n\tconsole.log(\"question id is :\"+this.questionId);\n\tconst no_id = this.questionId.substring(3);\n\tif(!arr1.includes(prev_question)){\n\t\tjQuery(\"#\"+this.questionId).hide();\n\t\tif(no_id % 3 != 0){\n\t\t\tthis.clickNextButton();\n\t\t}\n\t}\n\n});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});"

print("Creating the block and questions")
prev_prev_question_id = 'QID16'
with open(full_path+"/"+file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    block_dict={}
    block_number = 0
    question_kommentar_titel_js = "\n<p>&nbsp;</p>\n\n<p>&nbsp;</p>\n<button id=\"button\">Click to read full article</button>\n\n<div id=\"infodiv\" style=\"display:none;\">\n<strong><p>"
    question_titel_text_js = "</p>\n</strong>\n<p>"
    question_text_end_js = "</p>\n</div>"
    print("Reading each row")
    for row in csv_reader:
        # block_json['Description'] = row['Block'] #Uncomment if you are passing block from file.
        block_number += 1
        row_block = "Block "+str(block_number)
        block_json['Description'] = row_block
        # if row["Block"] not in block_dict: #Uncomment if you are passing block from file.
        if row_block not in block_dict:
            # print("Creating new block")
            while(True):
                response_block=create_block(survey_id=survey_id,data=block_json).json()
                block_dict[row_block] = response_block["result"]["BlockID"]
                if(response_block["meta"]["httpStatus"] == "200 - OK"):
                        break
            # block_dict[row['Block']] = response_block["result"]["BlockID"] #Uncomment if you are passing block from file.
                
            # print("response block is ")
            # print(response_block)

        # print("creating new question")
        question_json1['QuestionDescription'] = row['Kommentar']
        question_json1['QuestionText'] = row['Kommentar']+question_kommentar_titel_js+row["Titel"]+question_titel_text_js+row["Text"]+question_text_end_js
        # question_json['QuestionDescription'] = row["Question Text"]
        # question_json['QuestionText'] = row["Question Text"]
        # question_json["Choices"]["1"]['Display'] = row['Option 1'] #Uncomment if you are passing block from file.
        # question_json["Choices"]["2"]['Display'] = row['Option 2'] #Uncomment if you are passing block from file.
        # question_json["Choices"]["3"]['Display'] = row['Option 3'] #Uncomment if you are passing block from file.
        # question_json["QuestionID"] = row['Question'] #Uncomment if you are passing block from file.
        question_json1["DataExportTag"] = "Comment "+str(block_number)
        question_json1["QuestionType"] = "DB"
        question_json1["Selector"] = "TB"
        question_json1["QuestionJS"] = js_script
        # response_question = set_question(survey_id,block_dict[row['Block']],question_json).json()
        # print("****Printing ***")
        # print(question_json1)
        while(True):
            response_question = set_question(survey_id,block_dict[row_block],question_json1).json()
            # print("response of the create question is ")
            # print(response_question)
            if(response_question["meta"]["httpStatus"] == "200 - OK"):
                # print("Correct response")
                break
            

        prev_question_id = ''

        with open(full_path+"/"+hate_speech_file, mode='r') as hs_file:
            hs_csv_reader = csv.DictReader(hs_file)
            for row in hs_csv_reader:
                 hate_speech_json['QuestionDescription'] = row["Question Text"]
                 hate_speech_json['QuestionText'] = row["Question Text"]
                 hate_speech_json["Choices"]["1"]['Display'] = row['Option 1'] #Uncomment if you are passing block from file.
                 hate_speech_json["Choices"]["2"]['Display'] = row['Option 2'] #Uncomment if you are passing block from file.
                 hate_speech_json["Choices"]["3"]['Display'] = row['Option 3'] #Uncomment if you are passing block from file.
                 hate_speech_json["QuestionID"] = row['Question'] #Uncomment if you are passing block from file.
                 hate_speech_json["QuestionJS"] = js_script_hs
                 while(True):
                    response_question = set_question(survey_id,block_dict[row_block],hate_speech_json).json()
                    # print("response of the create question is ")
                    # print(response_question)
                    # print(response_question["meta"]["httpStatus"])
                    prev_question_id = response_question['result']['QuestionID']
                    if(response_question["meta"]["httpStatus"] == "200 - OK"):
                        # print("Correct response")
                        break
                    
                


        
        with open(full_path+"/"+hate_speech_file_2, mode='r') as hs_file_2:
            hs_csv_reader = csv.DictReader(hs_file_2)
            for row in hs_csv_reader:
                 hate_speech_json_2['QuestionDescription'] = row["Question Text"]
                 hate_speech_json_2['QuestionText'] = row["Question Text"]
                 hate_speech_json_2["Choices"]["1"]['Display'] = row['Option 1'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["2"]['Display'] = row['Option 2'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["3"]['Display'] = row['Option 3'] 
                 hate_speech_json_2["Choices"]["4"]['Display'] = row['Option 4'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["5"]['Display'] = row['Option 5'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["6"]['Display'] = row['Option 6'] 
                 hate_speech_json_2["Choices"]["7"]['Display'] = row['Option 7'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["8"]['Display'] = row['Option 8'] #Uncomment if you are passing block from file.
                 hate_speech_json_2["Choices"]["9"]['Display'] = row['Option 9'] 
                 hate_speech_json_2["Choices"]["10"]['Display'] = row['Option 10'] 
                 hate_speech_json_2["QuestionID"] = row['Question']
                 hate_speech_json_2["QuestionJS"] = js_script_hs
                #  print("Replacing json")
                #  print(hate_speech_json_2["DisplayLogic"]["0"]["0"]["ChoiceLocator"])
                #  print(type(hate_speech_json_2["DisplayLogic"]["0"]["0"]["ChoiceLocator"]))
                 hate_speech_json_2["DisplayLogic"]["0"]["0"]["ChoiceLocator"] = hate_speech_json_2["DisplayLogic"]["0"]["0"]["ChoiceLocator"].replace(prev_prev_question_id,prev_question_id)
                 hate_speech_json_2["DisplayLogic"]["0"]["0"]["LeftOperand"] = hate_speech_json_2["DisplayLogic"]["0"]["0"]["LeftOperand"].replace(prev_prev_question_id,prev_question_id)
                 hate_speech_json_2["DisplayLogic"]["0"]["0"]["QuestionID"] = hate_speech_json_2["DisplayLogic"]["0"]["0"]["QuestionID"].replace(prev_prev_question_id,prev_question_id)
                 hate_speech_json_2["DisplayLogic"]["0"]["0"]["QuestionIDFromLocator"] = hate_speech_json_2["DisplayLogic"]["0"]["0"]["QuestionIDFromLocator"].replace(prev_prev_question_id,prev_question_id)

                 while(True):
                    response_question = set_question(survey_id,block_dict[row_block],hate_speech_json_2).json()
                    # print("response of the create question is ")
                    # print(response_question)
                    prev_prev_question_id = prev_question_id
                    if(response_question["meta"]["httpStatus"] == "200 - OK"):
                        break
        






