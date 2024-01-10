import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class SendEmail:
    def __init__(self, mail_host, mail_user, mail_key, mail_send, receivers):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_key = mail_key
        self.mail_send = mail_send
        self.receivers = receivers

    # 只发送正文内容，不包含附件
    def send_email_by_text(self, context, Subject="自动化测试报告_纯文本"):
        message = MIMEText(context, 'plain', 'utf-8')
        message["Subject"] = Subject
        message["From"] = self.mail_send
        message["To"] = self.__to_receivers_convert(self.receivers)

        self.__login_and_send(message)

    def send_email_by_att(self, context, attachment_file_path=None, Subject="自动化测试报告_纯文本"):
        message = MIMEMultipart()

        text_body = MIMEText(context, 'plain', 'utf-8')
        message.attach(text_body)
        if attachment_file_path:
            Subject = "自动化测试报告_带附件"
            att_file = open(attachment_file_path, "rb")
            att = MIMEApplication(att_file.read())

            att_file_path = os.path.abspath(attachment_file_path)
            file_name = os.path.split(att_file_path)[1]
            att.add_header('content-disposition', 'attachment', filename=file_name)
            message.attach(att)

        message["Subject"] = Subject
        message["From"] = self.mail_send
        message["To"] = self.__to_receivers_convert(self.receivers)
        self.__login_and_send(message)

    def __login_and_send(self, message):
        smtp_obj = smtplib.SMTP(local_hostname="mail")
        smtp_obj.connect(self.mail_host, 25)
        smtp_obj.login(self.mail_user, self.mail_key)
        smtp_obj.sendmail(self.mail_send, self.receivers, message.as_string())
        smtp_obj.quit()

    # ['212703530@qq.com', 'deyunce@163.com']
    def __to_receivers_convert(self, to_receivers):
        if isinstance(to_receivers, list):
            receivers_str = ''
            for receiver in to_receivers:
                receivers_str = receivers_str + receiver + ';'

            return receivers_str
        else:
            print(f'{to_receivers}参数的值必须是列表')


if __name__ == '__main__':
    mail_host = 'smtp.qq.com'
    mail_user = '212703530'
    mail_key = "qhjfboyqejuvbiec"
    sender = '212703530@qq.com'
    receivers = ["940768986@qq.com", "lgmlovely@163.com"]
    send_email = SendEmail(mail_host, mail_user, mail_key, sender, receivers)
    send_email.send_email_by_att("自动化测试邮件封装_不带附件")
    send_email.send_email_by_att("自动化测试邮件封装_带附件", "attachment.log")
