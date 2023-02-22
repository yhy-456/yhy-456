import requests
import urllib3
import json
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from common.Log import *
from common.FileHelper import get_cookie
from urllib3.exceptions import InsecureRequestWarning

project_path = os.path.realpath(__file__).split("\common\\apiSend.py")[0].split("/common/apiSend.py")[0]
file_cookie = project_path + "/data/cookie.txt"

#传response对象，返回cookie的dict
def cookiedict(response_object):
    cookiedict = requests.utils.dict_from_cookiejar(response_object)
    return cookiedict

#返回response对象
def api_request(method,url,headers,parameters,verify=False,timeout=10,cookies=None,token=None):
    """
        封装请求
        :param method: 请求方式
        :param headers: 请求头
        :param url: 请求地址
        :param parameters: 请求参数
        :param verify： SSL证书验证
        :param timeout: 超时
        :param cookies: cookies（可传dict或cookiejar）
        :return:
    """
    urllib3.disable_warnings(InsecureRequestWarning)  # 去掉警告

    MyLog.info("请求方式：{}".format(method))
    MyLog.info("请求地址：{}".format(url))
    MyLog.info("请求头: {}".format(headers))
    MyLog.info("请求参数: {}".format(parameters))
    MyLog.info("SSL证书验证: {}".format(verify))
    MyLog.info("超时时长: {}".format(timeout))
    MyLog.info("cookies: {}".format(cookies))

    # print(headers)
    # print(method)
    # print(url)
    # print(parameters)
    if isinstance(headers,str):
        headers = json.loads(headers)
    if isinstance(parameters,str):
        parameters = json.loads(parameters)
    if token:
        headers['authorization'] = get_cookie(file_cookie)

    try:
        # get
        if method.lower() == 'get':
            response = requests.get(headers=headers,url=url,params=parameters,cookies=cookies,timeout=timeout,verify=verify)
            return response
            #print(response.text)

        # post
        elif method.lower() == 'post':
            #parameters = json.dumps(parameters)
            #json格式
            if type(parameters) == str:
                response = requests.post(headers=headers, url=url, data=parameters,cookies=cookies,timeout=timeout, verify=verify)
                return response
                # print(type(parameters))
                # print(response.text)
            #字典格式
            elif type(parameters) == dict:
                response = requests.post(headers=headers, url=url, json=parameters,cookies=cookies,timeout=timeout, verify=verify)
                return response
                # print(type(parameters))
                # print(parameters)
                # print(type(json.dumps(parameters)))
                # print(json.dumps(parameters))
                # print(response.text)
    except:
        MyLog.error('{},请求失败'.format(url))
        raise
        # print(response.cookies)
        # print(cookiedict(response.cookies))

#返回session对象
def seesion_request(method,url,headers,parameters,verify=False,timeout=10,cookies=None):
    """
        封装请求
        :param method: 请求方式
        :param headers: 请求头
        :param url: 请求地址
        :param parameters: 请求参数
        :param verify： SSL证书验证
        :param timeout: 超时
        :param cookies: cookies（可传dict或cookiejar）
        :return:
    """
    urllib3.disable_warnings(InsecureRequestWarning)  # 去掉警告
    MyLog.info("请求方式：{}".format(method))
    MyLog.info("请求地址：{}".format(url))
    MyLog.info("请求头: {}".format(headers))
    MyLog.info("请求参数: {}".format(parameters))
    MyLog.info("SSL证书验证: {}".format(verify))
    MyLog.info("超时时长: {}".format(timeout))
    MyLog.info("cookies: {}".format(cookies))

    if isinstance(headers,str):
        headers = json.loads(headers)
    if isinstance(parameters,str):
        parameters = json.loads(parameters)

    ssion = requests.session()
    try:
        # get
        if method.lower() == 'get':
            ssion.get(headers=headers, url=url, params=parameters,cookies=cookies,timeout=timeout, verify=verify)
            return ssion

        # post
        elif method.lower() == 'post':
            #json格式
            if type(parameters) == str:
                ssion.post(headers=headers, url=url, data=parameters,cookies=cookies,timeout=timeout, verify=verify)
                return ssion
            # 字典格式
            elif type(parameters) == dict:
                ssion.post(headers=headers, url=url, json=parameters,cookies=cookies,timeout=timeout, verify=verify)
                return ssion
    except:
        MyLog.error('{},请求失败'.format(url))
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
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjYyMDA0MjIyMSIsImNyZWF0ZWQiOjE2NzMyMzA1OTU2MzgsImV4cCI6MTY3NTgyMjU5NSwidXNlcm5hbWUiOiIxNjYyMDA0MjIyMSJ9.tGOo0qrRLlp5TbCpN7ItLSvtMKTneuM55QSbkyaXRJRtyG6ex3jADcQiEghnxK--DmbtE4dEZ57TW2faH4CbDA"
    }
    api_request(method,headers,url,parameters)
