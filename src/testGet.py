import configparser
import json

from src import webRequest

config = configparser.ConfigParser()
config.read("environment.ini")
host_patient = config.get('base', 'protocol') + '://' + config.get('base', 'host_patient')
print(host_patient)

patientToken = "6Vcy07lmq7HisiRhup5EZs9saM2WRu8snDOuMnKl"
# headers = {'content-type': 'application/json', "Authorization": patientToken}

headers = {"Authorization": patientToken}
result = webRequest.WebRequests.get(host_patient + '/v1/patients/profile', "", headers)

json_str = json.dumps(result)
data = json.loads(json_str)

print('code为：', data['code'])
print('message为：', data['message'])
print('data为：', data['data'])
