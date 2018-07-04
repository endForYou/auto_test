# coding=utf8
import requests
import re
from HReConf import dataConfig
import time
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')

# 适合发送和验证短信验证码所有地方


def sendCheckCode(
        session,
        account,
        source="1",
        sysType="1",
        action="1",
        notifyType="01"):
    # source     来源系统    1：default,dayhr,2：爱尚理客，3：canyin，4：dayfn，5：dayzp，6：hrre，7：tengxunyun，8：crm，9 ：dayjz，10:cscec，11:dayHRe，12:money，13：scm，14:omss
    # sysType    系统类型    1：PC WEB端， 2：iOS APP ，3：Android APP
    # action     动作        1：注册，2：找回密码，3：首次登录设置密码，4：验证手机号，5：修改手机号，6：体验，7：工资条，8：用户申请加入企业，9：绑定管理员
    # notifyType 通知类型    01：短信，02：邮件，03：语音
    # 获取图形验证码（此步骤有些地方一定需要）
    #url = dataConfig.reqUrlTest.TESTACCOUNT + "/authkaptcha/getKaptchaImage?Math.floor(Math.random()%20*%20100)"
    url = dataConfig.reqUrlTest.TESTACCOUNT + \
        "/kaptcha/image?" + str(int(time.time() * 1000))
    session.get(url)
    # 获取短信验证码接口
    url = dataConfig.reqUrlTest.TESTACCOUNT + "/account/webGetCode"
    # 处理万能图形验证码
    session.headers.update(
        {"X-QTP": "0", "content-type": "application/x-www-form-urlencoded; charset=UTF-8"})
    data = {
        "notifyType": notifyType,
        "source": source,
        "action": action,
        "account": account,
        "sysType": sysType,
        "identifycode": "8888"}
    response = session.post(url, data=data)
    text = response.text
    print text
    returnValue = text.encode("utf8")
    matchPattern = re.search("data\":\"(?P<checkCodeUuid>.*?)\"", returnValue)
    checkCodeUuid = matchPattern.group("checkCodeUuid")
    return checkCodeUuid


def verifyCheckCode(
        session,
        account,
        checkCodeUuid,
        checkCode,
        source="1",
        sysType="1",
        action="1",
        notifyType="01"):
    # source     来源系统    1：default,dayhr,2：爱尚理客，3：canyin，4：dayfn，5：dayzp，6：hrre，7：tengxunyun，8：crm，9 ：dayjz，10:cscec，11:dayHRO，12:money，13：scm，14:omss
    # sysType    系统类型    1：PC WEB端， 2：iOS APP ，3：Android APP
    # action     动作        1：注册，2：找回密码，3：首次登录设置密码，4：验证手机号，5：修改手机号，6：体验，7：工资条，8：用户申请加入企业，9：绑定管理员
    # notifyType 通知类型    01：短信，02：邮件，03：语音
    url = dataConfig.reqUrlTest.TESTACCOUNT + "/account/verifyCode"
    session.headers.update(
        {"content-type": "application/x-www-form-urlencoded; charset=UTF-8"})
    data = {
        "notifyType": notifyType,
        "source": source,
        "sysType": sysType,
        "action": action,
        "account": account,
        "code": checkCode,
        "uuid": checkCodeUuid}
    response = session.post(url, data=data)
    text = response.text
    print text
    returnValue = text.encode("utf8")
    flag = re.search(
        "\"retCode\":0",
        returnValue) and re.search(
        "正确",
        returnValue)
    if flag:
        return checkCode
    else:
        return None


if __name__ == "__main__":
    mobilePhone = "19856223241"
    session = requests.Session()
    checkCodeUuid = sendCheckCode(session, mobilePhone)
    verifyCheckCode(session, mobilePhone, checkCodeUuid)
