# qualtrics-automation
## This repo is part of Citizen Science Survey-
## 1. QualtricsAutomation
## 2. Citizen Science Backend (https://github.com/saurabhprasun20/citizen_science_backend)

#### Create a Qualtrics survey from csv documents.
#### There are two documents needed in order to compile the survey→
#### 1. Documents consisting of survey questions (e.g. Hate Speech in the first task) e.g. citizen_science_survey.csv
#### 2. Questions and options related to each question. e.g./src/data/hate_speech_question.csv and /src/data/hate_speech_question2.csv

#### Automate_qualtrics.py is executed to create the survey. It internally calls Qualtrics APIs for this purpose. 
#### These APIs like creating survey, adding questions need data in a particular json format. Thus Automate_qualtrics.py file provides these json in required format while calling these APIs.
#### To fulfill the format of json file, we are using pre defined json files. These files have been created before the experiment as per our requirement. Refer to the documentation for more details. 


