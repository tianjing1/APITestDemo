import unittest
import paramunittest
import readConfig
import writeConfig
from common import configHttp, common
from common.Log import MyLog
from testCase.patient.userLogin import testSendVerifyCode, testCheckVerifyCodeV2
from utilities import DateHelper
from utilities.SQLDataHelper import get_database_data

check_verify_code_xls = common.get_xls("patient_edge.xlsx", "getProfile")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


def get_profile(user_token):
    url = common.get_url_from_xml('getProfile')
    configHttp.set_url(url)
    header = {'authorization': user_token}
    configHttp.set_headers(header)
    return_json = configHttp.get()
    return return_json.json()


@paramunittest.parametrized(*check_verify_code_xls)
class GetProfile(unittest.TestCase):
    def setParameters(self,case_name, method, token, result, code, message, user_id,case_note):
        """
        set parameters
        :param case_note:
        :param case_name:用例名
        :param method:方法名
        :param token:用户身份
        :param result:返回结果
        :param code:返回结果code
        :param message:返回结果message
        :param user_id:返回结果的用户id
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.result = str(result)
        self.code = str(code)
        self.message = str(message)
        self.user_id = str(user_id)
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
        if self.user_id != "":
            sql = 'SELECT * FROM patient_app_service.user where user_id = ' + self.user_id
            user_info = get_database_data(sql)
            user_mobile = user_info['mobile'][0]
            testSendVerifyCode.send_verify_code(user_mobile)
            user_token = testCheckVerifyCodeV2.check_verify_code(user_mobile, "123456")
            print('写入的用户token为：', user_token)
            writeConfig.write_user_token('user_token', user_token)
        print("测试用例名为：" + self.case_name)

    def testGetProfile(self):
        """
        test body
        :return:
        """
        print("开始执行用例====================>>>>")
        # get url
        self.url = common.get_url_from_xml('getProfile')
        configHttp.set_url(self.url)
        print("第一步：设置url  " + self.url)

        # get visitor token
        if self.token == '1':
            token = writeConfig.read_user_token('user_token')
            print("用户token为：", token)
        elif self.token == '0':
            token = None

        # set headers
        header = {'authorization': token}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        body = {}
        configHttp.set_data(body)
        print("第三步：设置发送请求的参数", body)

        # test interface
        print("第四步：发送请求请求方法：")
        self.return_json = configHttp.get()

        # check result
        print("第五步：检查结果")
        self.checkResult()

    def tearDown(self):
        """
        :return:
        """
        pass
        self.log.build_case_line(self.case_name, str(self.info['code']), str(self.info['message']),
                                 str(self.info))
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
                print("[data]:", self.info['data'])
                sql = 'SELECT * FROM patient_app_service.user where user_id = ' + self.user_id
                user_info = get_database_data(sql)
                data = self.info['data']
                self.assertEqual(user_info['user_id'][0], data['user_id'])
                self.assertEqual(user_info['name'][0], data['name'])
                self.assertEqual(user_info['mobile'][0], data['mobile'])
                self.assertEqual(user_info['gender'][0], data['gender'])
                self.assertEqual(user_info['activated_state'][0], data['activated_state'])
                self.assertEqual(str(DateHelper.transform_date(str(user_info['birthday'][0])))[0:19],
                                 data['birthday'][0:19])

        if self.result != '200':
            self.assertEqual(self.code, str(self.info['code']))
            self.assertEqual(self.message, self.info['message'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
