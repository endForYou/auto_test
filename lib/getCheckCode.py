#coding=utf8
import requests
import re
from HReConf import dataConfig


def getCheckCodeOnline(mobilePhone):
    #访问生产环境OMSS的WEB页面，取出其中的手机验证码
    s = requests.session()
    url = "http://om.dayhr.com/login/check"
    data = {"account": "ding", "password": "ding"}
    s.post(url, data=data)

    #获取手机号码对应的短信消息列表
    url1 = "http://om.dayhr.com/msg-log/list"
    data = {"strStartDate": "", "strEndDate": "", "msgType": "0", "msgSendType": "0", "businessType": "0",
            "exceptionFlag": "-1", "msgReceiver": mobilePhone, "msgContent": "", "msgCode": "", "provider": "",
            "pageNo": "1", "pageSize": "20"}
    response = s.post(url1, data=data)
    text = response.text
    text = text.encode("utf8")

    #取出最新的一条记录id，即为需要的验证码
    checkCodeIdMatch = re.search("/msg-log/log-content/(?P<checkCodeId>\d+)\"", text)
    checkCodeId = checkCodeIdMatch.group("checkCodeId")

    #通过id，查询真正的验证码
    url2 = "http://om.dayhr.com/msg-log/log-content/" + checkCodeId
    response = s.post(url2)
    text = response.text
    text = text.encode("utf8")
    print text
    #取出验证码
    try:
        checkCodeMatch = re.search("验证码：(?P<checkCode>\d+)，", text)
        checkCode = checkCodeMatch.group("checkCode")
        return checkCode
    except:
        checkCodeMatch = re.search("初始密码 (?P<checkCode>\d+)", text)
        checkCode = checkCodeMatch.group("checkCode")
        return checkCode


def getCheckCode(mobilePhone, flag=dataConfig.reqUrlTest.CHECKCODEFLAG):
    #根据CHECKCODEFLAG的值来判断如何取验证码的值
    #flag=0时，表示从测试环境获取验证码，当前测试环境万能验证码为888888
    if flag == 0:
        checkCode = "888888"
        return checkCode
    #flag=1时，表示从生产环境获取验证码
    elif flag == 1:
        checkCode = getCheckCodeOnline(mobilePhone)
        return checkCode


if __name__ == "__main__":
    mobilePhone = "13993679989"
    print getCheckCode(mobilePhone, flag=1)

    #19487872230，初始密码 657557