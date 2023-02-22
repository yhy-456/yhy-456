import json
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from common.apiSend import api_request
from common.FileHelper import get_excel_data
from common.Log import MyLog
from jsoncomparison import Compare,NO_DIFF

class AssertHelper:
    def __init__(self):
        self.log = MyLog()

    def assert_json(self,result_json,check_json):
        if isinstance(result_json,str):
            result_json = json.loads(result_json)  #str转dict
        if isinstance(check_json,str):
            check_json = json.loads(check_json) #str转dict
        diff = Compare().check(result_json,check_json)   #json比较，有差异返回 差异值，没有则返回 {}
        try:
            self.log.info("result_json = {}".format(result_json))
            self.log.info("check_json = {}".format(check_json))
            assert diff == NO_DIFF
            MyLog.info("result_json == check_json")
            return True
        except:
            self.log.error("result_json != check_json，result_json为：{},check_json为：{}".format(result_json, check_json))
            raise


    def assert_code(self,result_code,check_code):
        try:
            assert result_code == check_code
            return True
        except:
            self.log.error("code断言错误，result_code为：{},check_code为：{}".format(result_code,check_code))
            raise

    def assert_text(self, result_text, check_text):
        try:
            assert result_text == check_text
            return True
        except:
            self.log.error("断言错误，result_text为：{},check_text为：{}".format(result_text, check_text))
            raise

    def assert_in_text(self, result_text, check_text):
        try:
            assert check_text in result_text  #result_text是否包含预期字符串（check_text）
            return True
        except:
            self.log.error("result_text不包含预期值check_text，result_text为：{},check_text为：{}".format(result_text, check_text))
            raise




if __name__ == '__main__':

    method = 'post'
    url = 'https://t-xiaofa-lawyer.aegis-info.com/mall-lawyer/activity/lottery/times/use'
    parameters = {
        "platform": "XIAOFA_MINGLV",
        "eventTypes": ["SHARE_ACTIVITY"],
        "activityId": 2,
        "beginTime": "2023-01-10 00:00:00",
        "endTime": "2023-01-10 23:59:59"
    }
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYyMDA0MjIyMSIsImNyZWF0ZWQiOjE2NzU4NDgyMzgzNzksImV4cCI6MTY3ODQ0MDIzOCwidXNlcm5hbWUiOiIxNjYyMDA0MjIyMSJ9.2fNiJ0GK6B5eTHAhg0uofvdM9raioQOx7_K8rncLqcCJEqiU65r_2eUfFcAIDAiWLA2st2qth9hlVeBCBQ3dtQ"
    }
    res = api_request(method, headers, url, parameters)
    file = "E:\\auto_test\\new_interface_auto\data\\test.xlsx"
    #print(get_excel_data(file, 'Sheet1', '用例1')[0]['实际结果'])
    #print(res.text)
    #b= json.loads(get_excel_data(file, 'Sheet1', '用例1')[0]['实际结果'])
    #c = json.loads(res.text)
    #print(type(b))
    # a=AssertHelper()
    # #a.assert_json(b,c)
    # b = a.assert_json(get_excel_data(file, 'Sheet1', '用例1')[0]['实际结果'], res.text)
    # print(b)

