import unittest
import paramunittest
import readConfig
from common import configHttp, common
from common.Log import MyLog

send_verify_code_xls = common.get_xls("patient_edge.xlsx", "sendVerifyCode")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


def send_verify_code(mobile):
    url = common.get_url_from_xml('sendVerifyCode')
    configHttp.set_url(url)
    header = {"Content-Type": "application/json"}
    configHttp.set_headers(header)
    body = {"mobile": mobile}
    configHttp.set_data(body)
    return_json = configHttp.postWithJson()
    return return_json.json()


@paramunittest.parametrized(*send_verify_code_xls)
class SendVerifyCode(unittest.TestCase):
    def setParameters(self, case_note,case_name, method, token, mobile, result, code, message):
        """
        set parameters
        :param case_note:
        :param case_name:
        :param method:
        :param token:
        :param mobile:
        :param result:
        :param code:
        :param message:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.mobile = str(mobile)
        self.result = str(result)
        self.code = str(code)
        self.message = str(message)
        self.return_json = None
        self.info = None

    def description(self):
        """
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        print("测试开始前准备====================>>>>")
        print("测试用例名为：" + self.case_name)

    def testSendVerifyCode(self):
        """
        test body
        :return:
        """
        print("开始执行用例====================>>>>")
        # get url
        self.url = common.get_url_from_xml('sendVerifyCode')
        configHttp.set_url(self.url)
        print("第一步：设置url  " + self.url)

        # get visitor token
        if self.token == '1':
            token = localReadConfig.get_headers("token_v")
        elif self.token == '0':
            token = None

        # set headers
        header = {"Content-Type": "application/json"}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        body = {"mobile": self.mobile}
        configHttp.set_data(body)
        print("第三步：设置发送请求的参数", body)

        # test interface
        print("第四步：发送请求请求方法：")
        self.return_json = configHttp.postWithJson()

        # check result
        print("第五步：检查结果")
        self.checkResult()

    def tearDown(self):
        """
        :return:
        """
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        # show return message
        self.info = self.return_json.json()
        print("接口返回的信息为：==========>>>>>>>>>")
        print("code", self.info['code'])
        print("message", self.info['message'])
        print("期望的code为：", self.code)
        if self.result == '200':
            self.assertEqual(str(self.info['code']), self.code)
            self.assertEqual(self.info['message'], self.message)

        if self.result != '200':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['message'], self.message)


if __name__ == "__main__":
    unittest.main(verbosity=2)
