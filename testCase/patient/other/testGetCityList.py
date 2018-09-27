import unittest
import paramunittest
import readConfig
from common import configHttp, common
from common.Log import MyLog

login_xls = common.get_xls("patient_edge.xlsx", "getCityList")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class GetCityList(unittest.TestCase):
    def setParameters(self, case_name, method, token, type, result, code, msg, case_note):
        """
        set parameters
        :param case_name:
        :param method:
        :param token:
        :param type:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.type = str(type)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
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
        print(self.case_name + "测试开始前准备")

    def testGetCity(self):
        """
        test body
        :return:
        """
        print("开始执行第一个用例==============>>>>>>>>>")
        # get url
        self.url = common.get_url_from_xml('getCityList')
        configHttp.set_url(self.url)
        print("第一步：设置url  " + self.url)

        # get visitor token
        if self.token == '1':
            token = localReadConfig.get_headers("token_v")
        elif self.token == '0':
            token = None

        # set headers
        header = {"authorization": str(token)}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        params = {"type": self.type}
        configHttp.set_params(params)
        print("第二步：设置发送请求的参数", self.type)

        # test interface
        print("第三步：发送请求请求方法：")
        self.return_json = configHttp.get()

        # check result
        print("第四步：检查结果")
        self.checkResult()

    def tearDown(self):
        """
        :return:
        """
        self.log.build_case_line(self.case_name, 'code', 'message')
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
        print("期望的code为：", self.code)
        print("message", self.info['message'])
        print("data", self.info['data'])

        print("表格中的result为：", self.result)
        if self.result == '200':
            self.assertEqual(str(self.info['code']), self.code)
            self.assertEqual(self.info['message'], self.msg)

        if self.result != '200':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
