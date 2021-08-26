#coding = utf-8
from email import encoders
#coding = utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
# from email.mime.multipart import MIMEBase
from email.mime.base import MIMEBase
import smtplib
from Config.ReadConfig import ReadConfig

import zipfile,os
import sys
GRANDFA = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(GRANDFA)
from Common.Logger import  WebLogger

import shutil
#自动发送邮件
class AutomaticeSendOfMail():
    def __init__(self,to_addr):
        self.from_addr = '1034781677@qq.com'       #你的邮箱
        self.password = 'qjqlqlvbaypqbbcb'      #密码
        self.to_addr = to_addr  #发送至谁的邮箱
        self.smtp_server = 'smtp.qq.com' #使用QQ邮箱发送
        self.log = WebLogger("邮件发送").logger

    def _format_addr(self,s):
        self.name, self.addr = parseaddr(s)
        return formataddr((Header(self.name, 'utf-8').encode(), self.addr))
    def sendMail(self):

        msg=MIMEMultipart()
        msg['From'] = self._format_addr('孙羽<%s>' % self.from_addr)
        msg['To'] = self._format_addr('自动化测试报告 <%s>' % self.to_addr)
        msg['Subject'] = Header('自动化测试', 'utf-8').encode()
        try:
            msg.attach(MIMEText('自动化测试报告,详情见附件', 'plain', 'utf-8'))

            with open(GRANDFA+'/Result/report.html','rb') as f:
                mime = MIMEBase('file','html',filename='report.html')
                mime.add_header('Content-Disposition', 'attachment', filename='report.html')
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
            #文件夹有文件,打包成zip添加至邮箱附件
            if os.listdir(GRANDFA+'/Result/caseScreenshot'):
                shutil.make_archive(GRANDFA+'/Result/picture','zip',GRANDFA+'/Result/caseScreenshot')
                with open('../result/picture.zip', 'rb') as f:
                    mimeZip = MIMEBase('file', 'zip', filename='picture.zip')
                    mimeZip.add_header('Content-Disposition', 'attachment', filename='picture.zip')
                    mimeZip.add_header('Content-ID', '<0>')
                    mimeZip.add_header('X-Attachment-Id', '0')
                    # 把附件的内容读进来:
                    mimeZip.set_payload(f.read())
                    # 用Base64编码:
                    encoders.encode_base64(mimeZip)
                    # 添加到MIMEMultipart:
                    msg.attach(mimeZip)

            server = smtplib.SMTP(self.smtp_server,25)
            #server.set_debuglevel(1)
            server.starttls()
            server.login(self.from_addr, self.password)
            server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
            server.quit()
            self.log.info("邮件发送成功,请及时查收!!!")
        except:
            self.log.info("邮件发送失败")




if __name__ == '__main__':
    to_email = ReadConfig().get_email("email")  # 获取需要发送的邮箱
    AutomaticeSendOfMail(to_email).sendMail()


