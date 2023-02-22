import os
import shutil
import sys
sys.path.append(os.path.dirname(sys.path[0]))

from common.config.config import Config
from common.FileHelper import *
from common.mkDir import *



def select_testcase():

    #判断testcase里是否存在模块目录
    #project_path = os.path.realpath(__file__).split("\common\CreateTestCase.py")[0]   #项目目录
    project_path = os.path.realpath(__file__).split("/common/CreateTestCase.py")[0].split("\common\CreateTestCase.py")[0]   #项目目录
    print(project_path)
    testcase_path = project_path + '/test_case/'    #testcase目录
    data_path = project_path + Config.get_value("directory", 'data_dir')  #测试数据目录
    file_path = data_path + 'testdata.xlsx'  #测试数据文件完整路径
    case_service_list = get_excel_sheet(file_path)    #获取测试文件的sheet名称列表
    template_file = testcase_path + 'Template.py'   #模板文件

    # 查看excel表的用例
    # 查看testcase目录的用例
    # 对比，testcase不存在则新增
    for service in case_service_list:    #sheet名称列表循环
        service_path = testcase_path+service     #服务的测试用例目录
        mk_dir(service_path)    #不存在则创建 服务的测试用例目录
        service_file = os.listdir(service_path)


        excel_case = get_excel_data(file_path,service)
        #excel_case1 = get_excel_data(file_path,service,'查询用户抽奖次数收支明细接口_001')
        #print(service,excel_case)
        #print(service,len(excel_case))
        #print(excel_case1)

        for i in range(0,len(excel_case)):  #循环遍历用例是否存在
            # print(service_file)
            # print(excel_case[i]['用例名称'])
            if excel_case[i]['用例名称'] + '.py' in service_file:    #如果不存在则复制文件
                pass
            else:
                new_case = service_path + '/' + excel_case[i]['用例名称'] + '.py'
                shutil.copyfile(template_file, new_case)
                set_file(new_case,'SheetName',service)
                set_file(new_case,'TestName',excel_case[i]['用例名称'])



if __name__ == '__main__':
    # print(os.path.realpath(__file__).split("\common\CreateTestCase.py")[0])
    # print(os.path.dirname(os.path.abspath(__file__)))
    select_testcase()
