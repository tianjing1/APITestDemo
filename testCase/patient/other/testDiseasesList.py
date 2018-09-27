import json
import unittest
import paramunittest
import readConfig
from common import configHttp, common
from common.Log import MyLog

login_xls = common.get_xls("patient_edge.xlsx", "getDiseasesList")
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class GetDiseasesList(unittest.TestCase):
    def setParameters(self, case_name, method, token, isCommon, name, parentCategoryId, categoryId, relatedDoctor, page,
                      pageSize, result, code, msg,case_note):
        """
        set parameters
        :param case_name:
        :param method:
        :param token:
        :param isCommon:
        :param name:
        :param parentCategoryId:
        :param categoryId:
        :param relatedDoctor:
        :param page:
        :param pageSize:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.isCommon = str(isCommon)
        self.name = str(name)
        self.parentCategoryId = str(parentCategoryId)
        self.categoryId = str(categoryId)
        self.relatedDoctor = str(relatedDoctor)
        self.page = str(page)
        self.pageSize = str(pageSize)
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

    def testGetDisease(self):
        """
        test body
        :return:
        """
        print("开始执行第一个用例==============>>>>>>>>>")
        # get url
        self.url = common.get_url_from_xml('getDiseasesList')
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
        params = {
            "isCommon": self.isCommon,
            "name": self.name,
            "parentCategoryId": self.parentCategoryId,
            "categoryId": self.categoryId,
            "relatedDoctor": self.relatedDoctor,
            "page": self.page,
            "pageSize": self.pageSize
        }
        configHttp.set_params(params)
        print("第二步：设置发送请求的参数", params)

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
        # info = self.info
        # if info['code'] == 0:
        #     # get user token
        #     token_u = common.get_value_from_return_json(info, 'member', 'token')
        #     # set user token to config file
        #     localReadConfig.set_headers("TOKEN_U", token_u)
        # else:
        #     pass
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
            s = json.dumps(self.info['data'])
            s1 = json.loads(s)
            print("获得的值为：", s1)
            print("list的长度", len(s1["list"]))
            for i in range(0, len(s1['list'])):
                print("第", i, "个list中的id为：", s1['list'][i]['id'])
                self.assertEqual(str(s1['list'][i]['id']), '3190')

        if self.result != '200':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
