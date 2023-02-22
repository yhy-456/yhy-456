from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from common.FileHelper import *

class Email:

    # def __init__(self,smtp_addr,sender_qq,pwd,receiver,
    #              title,send_email,content=None,file=None):
    #     self.smtp_addr = smtp_addr
    #     self.sender_qq = sender_qq
    #     self.pwd = pwd
    #     self.receiver = receiver
    #     self.title = title
    #     self.content = content
    #     self.file = file
    #     self.send_email = send_email

    def __init__(self,file):
       email_info =  get_yaml_data(file)
       self.smtp_addr = email_info["email"]["smtpserver"]
       self.sender_qq = email_info["email"]["sender_qq"]
       self.pwd = email_info["email"]["pwd"]
       self.receiver = email_info["email"]["receiver"]
       self.title = email_info["email"]["mail_title"]
       self.content = email_info["email"]["mail_content"]
       self.file = email_info["email"]["file"]
       self.send_email = email_info["email"]["sender_qq_mail"]



    def send_txt(self):
        # qq邮箱smtp服务器
        host_server = self.smtp_addr
        # sender_qq为发件人的qq号码
        sender_qq = self.sender_qq
        # pwd为qq邮箱的授权码
        pwd = self.pwd  ## xh**********bdc
        # 发件人的邮箱
        sender_qq_mail = self.send_email
        # 收件人邮箱
        receiver = self.receiver

        # 邮件的正文内容
        mail_content = self.content
        # 邮件标题
        mail_title = self.title

        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()