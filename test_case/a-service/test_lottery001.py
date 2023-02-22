import pytest
import allure
import json
from common.Log import *
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))


from common.config.config import Config
from common.FileHelper import *
from common.apiSend import *
from common.AssertHelper import AssertHelper


#project_path = os.path.realpath(__file__).split("\\test_case\\a-service\\test_lottery001.py")[0]   #项目目录
project_path = os.path.realpath(__file__).split("/test_case/a-service/test_lottery001.py")[0].split("\\test_case\\a-service\\test_lottery001.py")[0]   #项目目录
data_path = project_path + Config.get_value("directory", 'data_dir')  #测试数据目录
file_path = data_path + Config.get_value("test", 'testdata')

#case_data = get_excel_data(file_path,"test", "查询用户抽奖次数收支明细接口_001")
#a-service
case_data = get_excel_data(file_path, "a-service", "test_lottery001")

# print(case_data)
# @allure.epic(case_data['版本'])
# @allure.feature(case_data['ReqID'])
# @allure.story(case_data['用例标题'])
#@allure.title({cdata['用例标题']})

@pytest.mark.parametrize("cdata", case_data)
def test_lottery001(cdata):
    asserthelper = AssertHelper()
    description = "版本:{}|模块:{}|作者:{}|用例标题:{}".format(cdata['版本'], cdata['模块'], cdata['作者'], cdata['用例标题'])
    allure.dynamic.description(description)
    allure.dynamic.epic(cdata['版本'])
    allure.dynamic.feature(cdata['模块'])
    allure.dynamic.story(cdata['功能'])
    allure.dynamic.title(cdata['用例标题'])

    with allure.step("step1:发送请求并返回数据"):
        res=api_request(cdata['请求方式'], cdata['请求地址'], cdata['请求头'], cdata['请求参数'],token=cdata['token'])


    with allure.step("step2:校验返回状态"):
        asserthelper.assert_code(res.status_code,int(cdata['期望值']))
    with allure.step("step3:校验返回结果"):
        res_obj = json.loads(res.text)  #str转dict
        res_expect = json.loads(cdata['期望结果'])   #str转dict
        asserthelper.assert_code(res_obj['code'], res_expect['code'])
        asserthelper.assert_json(res_obj, res_expect)

        # logger.debug(res_obj["code"])
        # logger.debug(res_expect["code"])
        # print(res_obj["code"],res_expect["code"])
        # assert res_obj["code"] == res_expect["code"]
        # assert res_obj["message"] == res_expect["message"]
        # print(type(res.text['code']),type(cdata['期望结果']['code']))


    with allure.step("step4:校验数据库"):
        asserthelper.assert_text(1,cdata['数据库校验结果'])

