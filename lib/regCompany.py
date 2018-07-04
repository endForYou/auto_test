# coding=utf8
import requests
import re
import json
from HReConf import dataConfig
from HReLib import generateRandom
from HReLib import encodeUseJVM
from HReLib import getBeforeValue
from HReLib import webLogin, manageCheckCode
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')
#-----------------------------------------------------注册企业，返回企业注册成功后的session以及dd号


def companyReg(
        account,
        password,
        corpName,
        contactMobile,
        source="dayHRe"):
    contactPerson = "contact" + contactMobile
    s = requests.Session()

    # 获取短信验证码和验证短信验证码
    checkCodeUuid = manageCheckCode.sendCheckCode(s, account, "11" )
    checkCode = manageCheckCode.verifyCheckCode(
        s, account, checkCodeUuid)

    url = dataConfig.reqUrlTest.TESTACCOUNT + "/reg/companyreg"
    #------------------------------------调用jar包开始
    encodeAccount = encodeUseJVM.encodeUseJVM(account)
    encodePassword = encodeUseJVM.encodeUseJVM(password)
    #------------------------------------调用jar包结束
    encodeAccount = encodeAccount.encode("utf8")
    encodePassword = encodePassword.encode("utf8")

    #data = '{"account":"' + encodeAccount + '","pwd":"' + encodePassword + '","agpwd":"' + encodePassword + '","contactperson":"'+ contactPerson +'","corpname":"'+ corpName +'","contactmobile":"' + contactMobile + '","contactemail":"","industry":"","location":"","partnername":"","source":"' + source + '","channel":"","userExt1":"","userExt2":"","userExt3":"","userExt4":"","userExt5":"","guidance":0,"verifytype":"06"}'
    data = {
        "account": encodeAccount,
        "code": checkCode,
        "verifyCodeUuid": checkCodeUuid,
        "pwd": encodePassword,
        "agpwd": encodePassword,
        "contactperson": contactPerson,
        "corpname": corpName,
        "contactmobile": contactMobile,
        "contactemail": "",
        "industry": "",
        "location": "",
        "partnername": "",
        "source": "",
        "channel": "",
        "userExt1": "",
        "userExt2": "",
        "userExt3": "",
        "userExt4": "",
        "userExt5": "",
        "guidance": 0,
        "verifytype": "06",
        "verifyCodeAccount": contactMobile}
    s.headers.update({"content-type": "application/json;charset=UTF-8"})
    response = s.post(url, data=json.dumps(data))
    text = response.text
    print text
    returnValue = text.encode("utf8")
    # 取出DD号
    matchPattern = re.search("\"dd\":[\"]?(?P<CompanyDd>\d+)", text)
    CompanyDd = matchPattern.group("CompanyDd")

    # 登录
    login_result = webLogin.webLogin(account, source=source)

    if CompanyDd and login_result:
        return account
    else:
        return False
    # # 登录
    # loginUuidMatch = re.search("loginUuid\":\"(?P<loginUuid>.*?)\"", text)
    # loginUuid = loginUuidMatch.group("loginUuid")
    # url2 = dataConfig.reqUrlTest.TESTPASSPORT + \
    #     "/firstlogin?sourceurl=" + source + "&loginUuid=" + loginUuid
    # s.post(url2)
    #
    # url3 = dataConfig.reqUrlTest.TESTACCOUNT + \
    #     "/auth/message/corpmsg?source=" + source
    # s.post(url3)
    #
    # if source == "dayhr":
    #     url = dataConfig.reqUrlTest.TESTDAYHR + "/home/homeIndex/index.do"
    #     response = s.post(url)
    #     text = response.text
    #     returnValue = text.encode("utf8")
    #     expectValue = '"result":"true"'
    #
    #     s1 = webLogin.webLogin(account, password)
    #     if s1 and re.search(expectValue, returnValue) and checkCode:
    #         return CompanyDd
    #     else:
    #         return None
    #
    # if source == "aslk":
    #     url = "http://172.1.1.36:6767/param/selectByCorp.do"
    #     response = s.post(url)
    #     text = response.text
    #     returnValue = text.encode("utf8")
    #     expectValue = '"returnCode":0'
    #
    #     #s1 = webLogin.webLogin(account,password,source=source)
    #     if re.search(expectValue, returnValue) and checkCode:
    #         return CompanyDd
    #     else:
    #         return None


def companyRegWithPartner(
        account,
        password,
        corpName,
        contactMobile,
        industry,
        area,
        partner,
        source="dayhr"):
    contactPerson = "contact" + contactMobile
    s = requests.Session()

    # 获取短信验证码和验证短信验证码
    checkCodeUuid = manageCheckCode.sendCheckCodeForReg(s, contactMobile)
    checkCode = manageCheckCode.verifyCheckCodeForReg(
        s, contactMobile, checkCodeUuid)

    #------------------------------------调用jar包开始
    encodeAccount = encodeUseJVM.encodeUseJVM(account)
    encodePassword = encodeUseJVM.encodeUseJVM(password)
    #------------------------------------调用jar包结束
    encodeAccount = encodeAccount.encode("utf8")
    encodePassword = encodePassword.encode("utf8")

    # 获取所属行业、所在地区和推荐人
    url = dataConfig.reqUrlTest.TESTACCOUNT + "/basic/industrylist"
    response = s.post(url)
    text = response.text
    returnValue = text.encode("utf8")
    industryId = getBeforeValue.getBeforeValueExtra(
        industry, "id", "name", returnValue)

    url = dataConfig.reqUrlTest.TESTACCOUNT + "/basic/arealist"
    response = s.post(url)
    text = response.text
    returnValue = text.encode("utf8")
    areaId = getBeforeValue.getBeforeValueExtra(
        area, "id", "name", returnValue)

    url = dataConfig.reqUrlTest.TESTACCOUNT + "/basic/partnerlist"
    response = s.post(url)
    text = response.text
    returnValue = text.encode("utf8")
    partnerId = getBeforeValue.getBeforeValueExtra(
        partner, "id", "name", returnValue)

    url = dataConfig.reqUrlTest.TESTACCOUNT + "/reg/companyreg"
    data = '{"account":"' + encodeAccount + '","pwd":"' + encodePassword + '","agpwd":"' + encodePassword + '","contactperson":"' + contactPerson + '","corpname":"' + corpName + '","contactmobile":"' + contactMobile + '","contactemail":"","industry":"' + \
        industryId + '","location":"' + areaId + '","partnername":"' + partnerId + '","source":"' + source + '","channel":"","userExt1":"","userExt2":"","userExt3":"","userExt4":"","userExt5":"","guidance":0,"verifytype":"06"}'
    s.headers.update({"content-type": "application/json;charset=UTF-8"})
    response = s.post(url, data=data)
    text = response.text
    returnValue = text.encode("utf8")
    # 取出DD号
    matchPattern = re.search("\"dd\":[\"]?(?P<CompanyDd>\d+)", text)
    CompanyDd = matchPattern.group("CompanyDd")

    # 登录
    loginUuidMatch = re.search("loginUuid\":\"(?P<loginUuid>.*?)\"", text)
    loginUuid = loginUuidMatch.group("loginUuid")
    url2 = dataConfig.reqUrlTest.TESTPASSPORT + \
        "/firstlogin?sourceurl=" + source + "&loginUuid=" + loginUuid
    s.post(url2)

    url3 = dataConfig.reqUrlTest.TESTACCOUNT + \
        "/auth/message/corpmsg?source=" + source
    s.post(url3)

    if source == "dayhr":
        url = dataConfig.reqUrlTest.TESTDAYHR + "/home/homeIndex/index.do"
        response = s.post(url)
        text = response.text
        returnValue = text.encode("utf8")
        expectValue = '"result":"true"'

        s1 = webLogin.webLogin(account, password)
        if s1 and re.search(expectValue, returnValue) and checkCode:
            return CompanyDd
        else:
            return None

    if source == "aslk":
        url = "http://172.1.1.36:6767/param/selectByCorp.do"
        response = s.post(url)
        text = response.text
        returnValue = text.encode("utf8")
        expectValue = '"returnCode":0'

        #s1 = webLogin.webLogin(account,password,source=source)
        if re.search(expectValue, returnValue) and checkCode:
            return CompanyDd
        else:
            return None


if __name__ == "__main__":
    account = generateRandom.generateRandom("ttu")
    password = "b123456"
    corpName = generateRandom.generateRandom("深圳发展集团")
    contactMobile = generateRandom.generateRandom("194")
    companyReg(account, password, corpName, contactMobile)
