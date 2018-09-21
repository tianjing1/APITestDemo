#coding=utf-8
'''
Created on 2017-6-14
@author: 灵枢
Project:通过测试套件执行多个测试用例，并生成报告
'''
import unittest
import os,time

from common import HTMLTestRunnerNew

listaa = "/Users/nano/代码/Jessie/python/monitorAPI/testCase/patient"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="/Users/nano/代码/Jessie/python/monitorAPI/testCase/patient"+"result1.html"

fp=open(filename,'wb')
runner= HTMLTestRunnerNew.HTMLTestRunner(
    stream=fp,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：')
runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()