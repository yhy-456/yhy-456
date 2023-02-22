import pytest
import datetime
from common.CreateTestCase import *
from common.EmailHelper import *
from common.EmailYhy import *
from common.config.config import *


if __name__ == '__main__':
    #初始化测试用例
    select_testcase()

    #生成测试报告
    project_path = os.path.realpath(__file__).split("/run.py")[0].split(
        "\\run.py")[0]  #兼容linux执行

    args= [ '-s','-v',project_path+'/test_case/','--alluredir='+project_path+'/report/allure_raw','--clean-alluredir']
    pytest.main(args)

    cmd ='allure generate '+project_path+'/report/allure_raw -o '+project_path+'/report/allure_report -c '+project_path+'/report/allure_report'
    os.system(cmd)

    #执行sh脚本
    shell = 'sh '+project_path+'/report.sh'
    os.popen(shell)

    #发送邮件

    # sender = "user01@james.com"
    # receivers = ['user02@james.com']
    # to = '自动化测试'
    # mail_msg = """
    #     <p>""" + str(datetime.date.today()) + """的自动化测试结果，链接如下</p>
    #     <p><a href="http://192.168.188.29:8080/report/allure_report/index.html#">报告</a></p>
    #     """
    # s = EmailHelper(Config.get_value("email", 'host'), int(Config.get_value("email", 'ssl_port')), Config.get_value("email", 'user'), Config.get_value("email", 'password'))
    # s.message_html('message_subject', sender, to, mail_msg)
    # s.sendmail(sender, receivers)
    #
    #

    # test副本
    sender = "user01@james.com"
    receivers = ['user02@james.com']
    to = '自动化测试'
    mail_msg = """
        <p>""" + str(datetime.date.today()) + """的自动化测试结果，链接如下</p>
        <p><a href="http://192.168.188.29:8080/report/allure_report/index.html#">报告</a></p>
        """
    email = get_yaml_data_all("common/config/email.yaml")
    email2 = get_yaml_data("common/config/email.yaml")
    Email("common/config/email.yaml").send_txt()
    # s.message_html('message_subject', sender, to, mail_msg)
    # s.sendmail(sender, receivers)