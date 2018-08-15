import configparser
import requests


config = configparser.ConfigParser()
config.read("environment.ini")
host_operator = config.get('base', 'protocol') + '://' + config.get('base', 'host_operator')
print(host_operator)

# 接口的url
url = host_operator + "/api"

# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query": "test"
}

r = requests.request("post", url, params=params)

# 打印返回结果
print(r.text)

# 为了让结果看的更加清楚一点，我取来翻译的字段
import json
d = json.loads(r.text)
print(d['liju_result']['tag'])