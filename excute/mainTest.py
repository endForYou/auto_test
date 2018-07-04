# -*- coding: utf-8 -*-
import unittest
import requests
from HtmlTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# ======定义发送邮件========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('校管家接口自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('2837657131@qq.com', 'xxx336..')
    smtp.sendmail('2837657131@qq.com', '258048759@qq.com', msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')


# ======查找测试目录，找到最新生成的测试报告======
def new_report(test_report1):
    lists = os.listdir(test_report1)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_dir = "E:\\project\\python_project\\xgjInterfaceTest\\testcases"
    test_report = "E:\\project\\python_project\\xgjInterfaceTest\\report"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
    # 按照一定的格式获取当前的时间
    runner = HTMLTestRunner(output=test_report)
    runner.run(discover)
    # 运行测试

    # new_report = new_report(test_report)
    # send_mail(new_report)
