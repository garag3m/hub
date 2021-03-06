import requests
from requests.auth import HTTPBasicAuth
#Simple API request and post algorithm 
#Made by AdrielHigor

class Contador(object):
        def __init__(self, total):
            self.total = total

        def remains(self, done):
                left = (100 * done)/self.total
                return ("%.2f" % left)

#Simple request on suap's API.
api_request = requests.get('https://suap.ifpb.edu.br/api/ensino/alunos/v1/', auth=HTTPBasicAuth('Matricula', 'Senha') )

print(api_request.json())
#Getting response from 'api_request' as a json file.
response_init = api_request.json()

#API_ENDPOINT, show us where we are going to post our data responses in this case 'name', 'course', 'status', 'registration'
API_ENDPOINT = ("http://10.3.132.163:8000/api/students/")

#pagination varset
offset = 0

#Post count
student_count = 0
print(response_init["count"])
bytes = ((response_init["count"]))

porcentagem = Contador(bytes)
#A loop to pick all the responses from  the API and do the pagination based on the pages count of our API
for page in range (((response_init["count"])//100)+1):
    
    #Dinamic page request
    offset_request = requests.get('https://suap.ifpb.edu.br/api/ensino/alunos/v1/?offset={}'.format(offset), auth=HTTPBasicAuth('Matricula', 'Senha'))
    
    #Response handler
    response = offset_request.json()

    #Data storage and post into the API_ENDPOINT
    for student in response["results"]:
        
        if "Cajazeiras" in student["curso"]["nome"]:
            student_count +=1
            data = {
                'name': student["nome"], 
                'course':student["curso"]["nome"], 
                'status':student["situacao"], 
                'registration':student["matricula"]
                }

            student_post = requests.post(url = API_ENDPOINT, data=data, headers = {'Authorization': 'Token 11669ea2931bb635ed086869cd3c3c621e760c62'}) 

    offset += 100
    print('Page: ', offset)
    print('Registred students: ', student_count)
    print(porcentagem.remains(offset),'% complete;')
    print('==============================================================')

# name 
# course
# status
# registration

