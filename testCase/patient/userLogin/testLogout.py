import unittest
import paramunittest
import readConfig
from common import configHttp, common
from common.Log import MyLog
from testCase.patient.userLogin import testCheckVerifyCodeV2

logout_xls = common.get_xls("patient_edge.xlsx", "logout")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


def logout(token):
    url = common.get_url_from_xml('logout')
    configHttp.set_url(url)
    header = {"authorization": token, "Content-Type": "application/json"}
    configHttp.set_headers(header)
    body = {"unbind": 'true'}
    configHttp.set_data(body)
    return_json = configHttp.postWithJson()
    return return_json


@paramunittest.parametrized(*logout_xls)
class Logout(unittest.TestCase):
    def setParameters(self,case_name, method, token, mobile, mobile_code, unbind, result, code, message, deleted,case_note):
        """
        set parameters
        :param case_name:用例名
        :param method:方法名
        :param token:用户身份
        :param mobile:手机号
        :param mobile_code:验证码
        :param unbind:是否微信
        :param result:返回结果
        :param code:返回结果code
        :param message:返回结果message
        :param deleted:是否删除
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.mobile = str(mobile)
        self.mobile_code = str(mobile_code)
        self.unbind = str(unbind)
        self.result = str(result)
        self.code = str(code)
        self.message = str(message)
        self.deleted = str(deleted)
        self.return_json = None
        self.info = None
        self.user_token = None

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
        self.user_token = testCheckVerifyCodeV2.check_verify_code(self.mobile, self.mobile_code)
        print("用户的token为：" + self.user_token)
        print("测试用例名为：" + self.case_name)

    def testLogout(self):
        """
        test body
        :return:
        """
        print("开始执行用例====================>>>>")
        # get url
        self.url = common.get_url_from_xml('logout')
        configHttp.set_url(self.url)
        print("第一步：设置url  " + self.url)

        # get visitor token
        if self.token == '1':
            token = self.user_token
        elif self.token == '0':
            token = None

        # set headers
        header = {"authorization": token, "Content-Type": "application/json"}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        body = {"unbind": self.unbind}
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
        print("[code]:", self.info['code'])
        print("[message]:", self.info['message'])
        print("期望的code为：", self.code)
        if self.result == '200':
            self.assertEqual(self.code, str(self.info['code']))
            self.assertEqual(self.message, self.info['message'])
            if self.code == '1000000':
                self.assertEqual(self.deleted,str(self.info['data']['deleted']))

        if self.result != '200':
            self.assertEqual(self.code, str(self.info['code']))
            self.assertEqual(self.message, self.info['message'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
