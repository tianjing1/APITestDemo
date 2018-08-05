import requests
import json
data={
    'mobile':'18317119999'
}
headers = {
    'content-type':'application/json'
}
res = requests.post(url='http://services.dev.myzd.info/patient/api/login/sendVerifyCode',data=json.dumps(data),headers=headers)
print(res.text)




