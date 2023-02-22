import json
import xlrd3
import yaml
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from common.Log import *

def get_excel_data(dataFile,sheetName,funcname=None):
    """
    :param book: book对象
    :param sheet_data: sheet标签的数据
    :param sheet_data.nrows: 行数
    :param sheet_data.row_values(1): 获取第一行的数据
    :param sheet_data.ncols: 列数
    :param sheet_data.cell_value(0,1)：第0行第1列的数据
    """
    book =xlrd3.open_workbook(dataFile)        #获取文件的book对象
    sheet_data=book.sheet_by_name(sheetName)    #获取sheet标签的数据
    # print(book)
    # print(sheet_data)
    # print(sheet_data.row_values(1))

    case_data = []   #列表

    if funcname is None:
        for i in range(1,sheet_data.nrows):
            rowdata = {}
            for j in range(0,sheet_data.ncols):
                key = sheet_data.cell_value(0,j)
                if isinstance(sheet_data.cell_value(i, j), float):
                    value = int(sheet_data.cell_value(i, j))
                else:
                    value = sheet_data.cell_value(i, j)
                #print(key,value)
                rowdata[key] = value
            case_data.append(rowdata)
        #MyLog.debug(case_data)
        MyLog.debug("从'{}'文件中的'{}'工作表获取到的所有数据：{}".format(dataFile, sheetName,case_data))
        return case_data
    else:
        for i in range(0,sheet_data.nrows):
            rowdata = {}
            if sheet_data.row_values(i)[3] == funcname:
                for j in range(0,sheet_data.ncols):
                    key = sheet_data.cell_value(0,j)
                    if isinstance(sheet_data.cell_value(i,j),float):
                        value = int(sheet_data.cell_value(i,j))
                    else:
                        value = sheet_data.cell_value(i, j)
                    rowdata[key] = value
                case_data.append(rowdata)
        MyLog.debug("从'{}'文件中的'{}'工作表获取到'{}'的'{}'的所有数据：{}".format(dataFile,sheetName,sheet_data.cell_value(0,2),funcname,case_data))
        #MyLog.debug(case_data)
        return case_data


def get_excel_sheet(dataFile):
    book = xlrd3.open_workbook(dataFile)
    return book.sheet_names()

def get_yaml_data(file):
    with open(file,'r',encoding='utf-8') as f:
        return yaml.load(f,yaml.Loader)

def get_yaml_data_all(file):
    with open(file,'r',encoding='utf-8') as f:
        return list(yaml.load_all(f,yaml.Loader))


def get_json_data(file):
    with open(file,'r',encoding='utf-8') as f:
        return json.load(f)


def get_cookie(file):
    with open(file,'r',encoding='utf-8') as f:
        return f.read()

def set_cookie(file,value):
    with open(file,'w+',encoding='utf-8') as f:
        f.write(value)

#def set_file(file):
def set_file(file,pipei,gengxin):
    with open(file,'r',encoding='utf-8') as fw:
        source = fw.readlines()
    with open(file,'w+',encoding='utf-8') as f:
        for line in source:
            if pipei in line:
                line = line.replace(pipei,gengxin)
                f.write(line)
            else:
                f.write(line)



if __name__=='__main__':
    file = "E:\\auto_test\\new_interface_auto\data\\test.xlsx"
    file_yaml = "E:\\auto_test\\new_interface_auto\data\\Token.yml"
    file_json = "E:\\auto_test\\new_interface_auto\data\\test.json"
    #print(get_excel_data(file,'Sheet1','用例2'))
    #print(get_yaml_data_all(file_yaml))
    #print(get_json_data(file_json))
    #print(type(get_json_data(file_json)))
    file_cookie = "E:\\auto_test\\new_interface_auto\data\\cookie.txt"
    #set_cookie(file_cookie,'aaaaaaaaaaa')
    # b = {}
    # a= get_cookie(file_cookie)
    # b['a'] = a
    # print(b)
    #print(a)
    # with open(file_cookie) as f:
    #     print(f.readlines())
    file = "E:\\auto_test\\new_interface_auto\data\\testdata.xlsx"
    # get_excel_sheet(file)
    #case_data = get_excel_data(file, "test", "告警上报_001")
    #print(case_data)

    # file = "E:\\auto_test\\new_interface_auto\\test_case\\Template.py"
    # set_file(file)

    case_data = get_excel_data(file, "test", "test_times001")




