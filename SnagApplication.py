#Kyle Archuleta - Snag Application Code Review 


import json
import os

# Questions to be added, removed or edited by product owner

questions = [

	{'Id' : 'id1' , 'Question' : 'Do you know Python?' , 'Answer' : ['yes' , 'y']}, 
	{'Id' : 'id2' , 'Question' : 'Do you know Java?' , 'Answer' : ['yes' , 'y']},
	{'Id' : 'id3' , 'Question' : 'Are you over 18 years of age?' , 'Answer' : ['yes' , 'y']}, 
	{'Id' : 'id4' , 'Question' : 'Do you require a work visa?' , 'Answer' : ['no' , 'n']},
	{'Id' : 'id5' , 'Question' : 'Are you excited about new technology?' , 'Answer' : ['yes' , 'y']}
	
	]
	
#ensure applicants have all required questions	
size = len(questions)

#path to applicant files
#With no database opting to read files in current directory 

path = os.getcwd()
successful = []

def applicants():
    #ingest applicant data
    for name in os.listdir(path):
        if(name.endswith('.json')):
            with open(name) as json_data:
                count = 0
                applicant = json.load(json_data)
                #Any applicant who did not answer all N questions is disqualified
                if(len(applicant['Questions']) < size): break
                for item in applicant['Questions']:
                    #ensure answer is lowercase to match answer key
                    item['Answer'] = item['Answer'].lower()
                    for index in questions:
                        if item['Id'] == index['Id']:
                            for i in index['Answer']:
                                if item['Answer'] == i:
                                    count += 1
                                    break
                if count == 5:
                    successful.append(applicant['Name'])

applicants()

f = open('validApplicants.txt', 'w')
f.write('Meets qualifications:\n')
for i in successful:
    f.write(i)
    f.write('\n')
