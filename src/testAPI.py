import requests
import json

from src import webRequest

# data={
#     'mobile':'18317119999'
# }
# headers = {
#     'content-type':'application/json'
# }
# res = requests.post(url='http://services.dev.myzd.info/patient/api/login/sendVerifyCode',data=json.dumps(data),headers=headers)
# print(res.text)


result = webRequest.WebRequests.get("http://services.dev.myzd.info/patient/api/v1/cities?type=DOCTOR", "type=DOCTOR", {'content-type': 'application/json'})
json_str = json.dumps(result)
data = json.loads(json_str)
code = data['code']
print('code为：',code)
print('message为：',data['message'])
print('data为：',data['data'])

result1 = webRequest.WebRequests.post_json("http://services.dev.myzd.info/patient/api/login/sendVerifyCode",{'mobile':'18317119999'},{'content-type': 'application/json'})
json_str1 = json.dumps((result1))
data = json.loads(json_str)
code1 = data['code']
print('code为',code1)

result = webRequest.WebRequests.get("http://services.dev.myzd.info/patient/api/v1/diseaseCategories", "", {'content-type': 'application/json'})
json_str = json.dumps(result)
data = json.loads(json_str)
code = data['code']
print('code为：',code)
print('message为：',data['message'])
print('data为：',data['data'])


url = "http://services.dev.myzd.info/patient/api/v1/diseaseCategories"
headers = {'content-type': 'application/json'}
result = webRequest.WebRequests.get(url, "", headers)
json_str = json.dumps(result)
data = json.loads(json_str)
code = data['code']
print('code为：',code)
print('message为：',data['message'])
print('data为：',data['data'])





