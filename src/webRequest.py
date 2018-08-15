import requests
import json
import logging


class WebRequests:
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.INFO)

    @staticmethod
    def get(url, para, headers):
        try:
            logging.info("发送请求：===>>  " + url)
            logging.info("请求数据：===>>  " + para)
            r = requests.get(url=url, params=para, headers=headers)
            logging.info("等待回应：===>>  " + str(r.status_code) + " " + str(r.reason))
        except BaseException as e:
            print("请求失败", str(e))
        return r.json()

    @staticmethod
    def post_json(url, para, headers):
        try:
            data = json.dumps(para)
            r = requests.post(url=url, data=data, headers=headers)
            return r.json()
        except BaseException as e:
            print("请求失败", str(e))

    @staticmethod
    def post(url, para, headers):
        try:
            r = requests.post(url=url, data=para, headers=headers)
            return r.json()
        except BaseException as e:
            print("请求失败", str(e))
