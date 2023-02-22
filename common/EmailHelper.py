import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class EmailHelper:
    def __init__(self,host,port,user,password):
        if port == 465:
            self.smtp = smtplib.SMTP_SSL(host, port)
            self.smtp.login(user=user, password=password)
        elif port == 25:
            self.smtp = smtplib.SMTP(host,port)
            self.smtp.login(user=user, password=password)
        else:
            print("输入正确的host和port")
    #文本
    def message_text(self,message_subject,from_user,to_user,message_content):
        self.message = MIMEText(message_content, 'plain', 'utf-8')  # 邮件内容
        self.message['From'] = Header(from_user, 'utf-8')  # 发件人的昵称
        self.message['To'] = Header(to_user, 'utf-8')  # 收件人的昵称
        self.message['Subject'] = Header(message_subject, 'utf-8')  # 定义邮件标题



    def message_html(self,message_subject,from_user,to_user,message_content):
        self.message = MIMEText(message_content, 'html', 'utf-8')   #邮件内容
        self.message['From'] = Header(from_user, 'utf-8')  # 发件人的昵称
        self.message['To'] = Header(to_user, 'utf-8')  # 收件人的昵称
        self.message['Subject'] = Header(message_subject, 'utf-8')  # 定义邮件标题

    def message_attr(self, message_subject, from_user, to_user, message_content,file):
        self.message = MIMEMultipart()   #创建一个带附件的实例
        self.message['From'] = Header(from_user, 'utf-8')  # 发件人的昵称
        self.message['To'] = Header(to_user, 'utf-8')  # 收件人的昵称
        self.message['Subject'] = Header(message_subject, 'utf-8')  # 定义邮件标题
        self.message.attach(MIMEText(message_content, 'plain', 'utf-8')) #邮件正文内容
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        self.message.attach(att1)



    def sendmail(self,sender, receivers):
        try:
            self.smtp.sendmail(sender, receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

if __name__ == '__main__':
    host = "192.168.188.29"
    ssl_port = 465
    user = "user01@james.com"
    password = 'user01'
    sender = "user01@james.com"
    receivers = ['user02@james.com','user03@james.com']
    to='测试'

    receivers_list = [('user02@james.com','user02'),('user03@james.com','user03')]
    mail_msg = """
    <p>"""+str(datetime.date.today()) + """的自动化测试结果，链接如下</p>
    <p><a href="http://192.168.188.29:8080/report/allure_report/index.html#">报告</a></p>
    """
    file = 'E:/auto_test/new_interface_auto/common/remake.txt'
    s= EmailHelper(host,ssl_port,user,password)
    #s.message_text('message_subject',sender,to,'message_title')
    s.message_html('message_subject', sender, to, mail_msg)
    # s.message_attr('message_subject',sender,str(receivers),'message_content',file)
    s.sendmail(sender,receivers)
    #s.sendmail_text()
    #print(type(receivers_list))
    #print(receivers_list[0][0])
    #print(len(receivers_list))

    # for i in range(0,len(receivers_list)):
    #     print(receivers_list[i][0])
    #     print(receivers_list[i][1])
