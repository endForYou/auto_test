# coding=utf8
import json
from random import randint
from time import time
import requests
import re
from HReConf import dataConfig
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')


def webLogin(account, password='b123456', source="dayhr"):
    try:
        # 创建session，用于存储会话过程中所有的sessionId
        s = requests.Session()
        # 打开dayHr首页
        url = dataConfig.reqUrlTest.TESTPASSPORT + "/login?source=" + source
        response = s.post(url, timeout=30)
        text = response.text
        # 取出lt、jsessionid、uuid，供登录接口调用
        patternValue = re.search(
            "name=\"lt\" value=\"(?P<LT>.*?)\".*name=\"qruuid\" value=\"(?P<UUID>.*?)\".*jsessionid=(?P<JSESSIONID>\w+?)\"",
            text,
            re.M | re.DOTALL)
        LT = patternValue.group("LT")
        UUID = patternValue.group("UUID")
        JSESSIONID4 = patternValue.group("JSESSIONID")

        # 调用登录接口进行登录
        urlLogin = dataConfig.reqUrlTest.TESTPASSPORT + \
            "/login;jsessionid=" + str(JSESSIONID4)
        data = {
            "username": account,
            "account": account,
            "password": password,
            "lt": LT,
            "qruuid": UUID,
            "remfor_input": "1",
            "execution": "e1s1",
            "_eventId": "submit",
            "sourceurl": source}
        r = s.post(urlLogin, data=data, timeout=30)
        loginReturn = r.text

        #===========================================================================================以前老的流程，已经废弃
        # #取出企业邀请地址
        # service = re.search("window.location.href=\"(?P<SERVICE>.*).{3}\s</script>",loginReturn)
        # serviceValue = service.group("SERVICE")
        # #请求中加入企业邀请地址，此处用于处理有企业邀请列表的情况
        # urlLogin2 = dataConfig.reqUrlTest.TESTPASSPORT + "/login?service="+serviceValue
        # r1 = s.post(urlLogin2,timeout=30)
        # text = r1.text
        # text = text.encode("utf8")
        #======================================================================
        # 根据source的不同进行不同的跳转和判断
        url = dataConfig.reqUrlTest.TESTACCOUNT + \
            "/auth/message/corpmsg?source=" + source
        response = s.post(url)
        text = response.text

        expectValue = '"result":"true"'

        if source == "dayhr":
            url = "http://www.dayhr.com/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "money":
            url = "https://pay.daydao.com/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "omss":
            url = "http://om.daydao.com/omss/home/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "aslk":
            if dataConfig.reqUrlTest.CHECKCODEFLAG == 0:
                url = "http://172.1.1.36:6767/views/index.jsp#!crm/salesboard/salesboard"
            elif dataConfig.reqUrlTest.CHECKCODEFLAG == 1:
                url = "http://www.idaycrm.com/views/index.jsp#!crm/salesboard/salesboard"
            response = s.post(url, timeout=30)
            text = response.text
            returnValue = text.encode("utf8")
            # 在返回的页面中查找empId值
            matchPatternEmpId = re.search(
                "empId[\"]?:[\"]?(?P<empId>\d+?)",
                returnValue,
                re.M | re.DOTALL)
            matchPatternCorpId = re.search(
                "corpId[\"]?:[\"]?(?P<corpId>\d+)",
                returnValue,
                re.M | re.DOTALL)

            if matchPatternEmpId and matchPatternCorpId:
                corpId = matchPatternCorpId.group("corpId")
                empId = matchPatternEmpId.group("empId")
                return s, corpId, empId
            else:
                return None

        if source == "dayscm":
            returnValue = text.encode("utf8")
            if re.search(
                    "个人信息",
                    returnValue) and re.search(
                    "您好,",
                    returnValue):
                return s
            else:
                return None

        if source == "canyin":
            url = "http://canyin.daydao.com/daycanyin/canyin/sys/menu1/retMenuList"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "dayHRe":
            url = "http://hre.daydao.com/dayhre/horcorp/selectById"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None
        if source == "demoerp":
            url = "http://ec.daydao.com/demoerp/scm/manage/dashboard/baseFlow?tabPageId=jerichotabiframe_0"
            response = s.post(url)
            expectValue = u"采购管理"

            text = response.text
            if re.search(expectValue, text):
                return s
            else:
                return None
        if source == "dayjz":
            return s
    except BaseException:
        return None


def webLoginChooseAdmin(account, password='b123456', source="dayhr"):
    try:
        # 创建session，用于存储会话过程中所有的sessionid
        s = requests.Session()
        # 打开dayhr首页
        url = dataConfig.reqUrlTest.TESTPASSPORT + "/login?source=" + source
        response = s.post(url, timeout=30)
        text = response.text
        # 取出lt、jsessionid、uuid，供登录接口调用
        patternValue = re.search(
            "name=\"lt\" value=\"(?P<LT>.*?)\".*name=\"qruuid\" value=\"(?P<UUID>.*?)\".*jsessionid=(?P<JSESSIONID>\w+?)\"",
            text,
            re.M | re.DOTALL)
        LT = patternValue.group("LT")
        UUID = patternValue.group("UUID")
        JSESSIONID4 = patternValue.group("JSESSIONID")

        # 调用登录接口进行登录
        urlLogin = dataConfig.reqUrlTest.TESTPASSPORT + \
            "/login;jsessionid=" + str(JSESSIONID4)
        data = {
            "username": account,
            "account": account,
            "password": password,
            "lt": LT,
            "qruuid": UUID,
            "remfor_input": "1",
            "execution": "e1s1",
            "_eventId": "submit",
            "sourceurl": source}
        r = s.post(urlLogin, data=data, timeout=30)
        loginReturn = r.text
        #===========================================================================================以前老的流程，已经废弃
        # #取出企业邀请地址
        # service = re.search("window.location.href=\"(?P<SERVICE>.*).{3}\s</script>",loginReturn)
        # serviceValue = service.group("SERVICE")
        # #请求中加入企业邀请地址，此处用于处理有企业邀请列表的情况
        # urlLogin2 = dataConfig.reqUrlTest.TESTPASSPORT + "/login?service="+serviceValue
        # r1 = s.post(urlLogin2,allow_redirects=True,timeout=30)
        # text = r1.text
        #======================================================================
        # 根据source的不同进行不同的跳转和判断
        url = dataConfig.reqUrlTest.TESTACCOUNT + \
            "/auth/message/corpmsg?source=" + source
        response = s.post(url)
        text = response.text

        data = {'userType': '04'}
        url = dataConfig.reqUrlTest.TESTACCOUNT + "/auth/message/selectUserType"
        response = s.post(url, data=data)
        text = response.text

        # 获取loginUuid
        loginUuidMatch = re.search("loginUuid\":\"(?P<loginUuid>.*?)\"", text)
        loginUuid = loginUuidMatch.group("loginUuid")

        # 自动登录
        url = dataConfig.reqUrlTest.TESTPASSPORT + \
            "/firstlogin?sourceurl=dayhr&loginUuid=" + loginUuid
        response = s.post(url)
        text = response.text

        url = dataConfig.reqUrlTest.TESTACCOUNT + \
            "/auth/message/corpmsg?source=" + source
        response = s.post(url)
        text = response.text

        expectValue = '"result":"true"'

        if source == "dayhr":
            url = dataConfig.reqUrlTest.TESTDAYHR + "/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            print text
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "money":
            url = "https://pay.daydao.com/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "omss":
            url = "http://om.daydao.com/omss/home/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None
    except BaseException:
        return None


def webLoginChoosePerson(account, password='b123456', source="dayhr"):
    try:
        # 创建session，用于存储会话过程中所有的sessionid
        s = requests.Session()
        # 打开dayhr首页
        url = dataConfig.reqUrlTest.TESTPASSPORT + "/login?source=" + source
        response = s.post(url, timeout=30)
        text = response.text
        # 取出lt、jsessionid、uuid，供登录接口调用
        patternValue = re.search(
            "name=\"lt\" value=\"(?P<LT>.*?)\".*name=\"qruuid\" value=\"(?P<UUID>.*?)\".*jsessionid=(?P<JSESSIONID>\w+?)\"",
            text,
            re.M | re.DOTALL)
        LT = patternValue.group("LT")
        UUID = patternValue.group("UUID")
        JSESSIONID4 = patternValue.group("JSESSIONID")

        # 调用登录接口进行登录
        urlLogin = dataConfig.reqUrlTest.TESTPASSPORT + \
            "/login;jsessionid=" + str(JSESSIONID4)
        data = {
            "username": account,
            "account": account,
            "password": password,
            "lt": LT,
            "qruuid": UUID,
            "remfor_input": "1",
            "execution": "e1s1",
            "_eventId": "submit",
            "sourceurl": source}
        r = s.post(urlLogin, data=data, timeout=30)
        loginReturn = r.text
        #===========================================================================================以前老的流程，已经废弃
        # #取出企业邀请地址
        # service = re.search("window.location.href=\"(?P<SERVICE>.*).{3}\s</script>",loginReturn)
        # serviceValue = service.group("SERVICE")
        # #请求中加入企业邀请地址，此处用于处理有企业邀请列表的情况
        # urlLogin2 = dataConfig.reqUrlTest.TESTPASSPORT + "/login?service="+serviceValue
        # r1 = s.post(urlLogin2,allow_redirects=True,timeout=30)
        # text = r1.text
        #======================================================================
        # 根据source的不同进行不同的跳转和判断
        url = dataConfig.reqUrlTest.TESTACCOUNT + \
            "/auth/message/corpmsg?source=" + source
        response = s.post(url)
        text = response.text

        data = {'userType': '05'}
        url = dataConfig.reqUrlTest.TESTACCOUNT + "/auth/message/selectUserType"
        response = s.post(url, data=data)
        text = response.text

        # 获取loginUuid
        loginUuidMatch = re.search("loginUuid\":\"(?P<loginUuid>.*?)\"", text)
        loginUuid = loginUuidMatch.group("loginUuid")

        # 自动登录
        url = dataConfig.reqUrlTest.TESTPASSPORT + \
            "/firstlogin?sourceurl=dayhr&loginUuid=" + loginUuid
        response = s.post(url)
        text = response.text

        url = dataConfig.reqUrlTest.TESTACCOUNT + \
            "/auth/message/corpmsg?source=" + source
        response = s.post(url)
        text = response.text

        expectValue = '"result":"true"'

        if source == "dayhr":
            url = dataConfig.reqUrlTest.TESTDAYHR + "/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            print text
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "money":
            url = "https://pay.daydao.com/home/homeIndex/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None

        if source == "omss":
            url = "http://om.daydao.com/omss/home/index.do"
            response = s.post(url)
            text = response.text.encode("utf8")
            if re.search(expectValue, text):
                return s
            else:
                return None
    except BaseException:
        return None


def audit(number):
    query_url = "http://ec.daydao.com/demoerp/scm/order/orderAudit/"
    audit_url = "http://ec.daydao.com/demoerp/scm/order/orderAudit/autoAudit"
    pattern_id = r'data-id="(\d*)"'
    query_data = {
        "pageNo": 1,
        "pageSize": number
    }
    query_response = s.post(query_url, query_data)
    match = re.findall(pattern_id, query_response.text)
    if number < 150:
        data = {
            "ids": match[0],
            "cancelReason": "",
            "forceAuditPwd": ""
        }
        ids = str(match[0])
        length = 1
    else:
        length = len(match)
        ids = ",".join(match)
        data = {
            "ids": ids,
            "cancelReason": "",
            "forceAuditPwd": ""
        }
    print "%d个审核的id为:%s" % (length, ids)
    time1 = time()
    audit_result = s.post(audit_url, data)
    if re.search(u"审核成功", audit_result.text):
        time2 = time()
        print "审核时间为：" + str(time2 - time1)
        return match
    else:
        print "%d个订单审核失败" % length
        return False


def batch_shipment(s, number=150):
    query_url = "http://ec.daydao.com/demoerp/scm/order/orderPrint/"
    shipment_url = "http://ec.daydao.com/demoerp/scm/order/orderPrint/batchShipment"
    pattern_id = r"data-shipmentId='(\d*)'"
    all_ids = ""
    if number < 150:
        number = 150
    count = number / 150
    remainder = number % 150
    for i in range(0, count):
        query_data = {
            "pageNo": i + 1,
            "pageSize": 150,
            "status": 500
        }
        query_result = s.post(query_url, query_data)
        match = re.findall(pattern_id, query_result.text)
        ids = ",".join(match)
        all_ids += ids
    if remainder > 0:
        query_data = {
            "pageNo": count + 1,
            "pageSize": 150,
            "status": 500
        }
        query_result = s.post(query_url, query_data)
        match = re.findall(pattern_id, query_result.text)
        ids = ",".join(match[0:remainder])
        all_ids += ids
    data = {
        "ids": all_ids
    }
    time3 = time()
    shipment = s.get(shipment_url, params=data)
    print shipment.text
    if re.search(u"发货成功：%d条；发货失败：0条" % number, shipment.text):
        time4 = time()
        print "批量发货时间为：" + str(time4 - time3)
    else:
        match = re.findall(u"发货成功：\d+条；发货失败：(\d+)条", shipment.text)
        print match
        print "%s个订单批量发货失败" % match[0]


def fill_waybill(s, page):
    query_url = "http://ec.daydao.com/demoerp/scm/order/orderPrint/"
    for i in range(18, page + 1):
        query_data = {
            "pageNo": i,
            "pageSize": 150,
            "status": 500,
        }
        pattern_id = r'data-id="(\d*)"'
        query_result = s.post(query_url, query_data)
        match = re.findall(pattern_id, query_result.text)
        ids_list = match
        print match
        fill_url = "http://ec.daydao.com/demoerp/scm/order/orderPrint/savePaperLogistics"
        order_list = []
        random_number = randint(100000, 999999)
        print random_number
        number = len(ids_list)
        for i in range(0, number):
            data = {
                "id": ids_list[i],
                "primaryWaybillCode": str(random_number + i)
            }
            order_list.append(data)
        order_list_json = json.dumps(order_list)
        order_list_dic = {
            "orderList": order_list_json
        }
        order_list_json = json.dumps(order_list_dic)
        print order_list_json
        fill_result = s.post(fill_url, data=order_list_dic)
        result_dic = json.loads(fill_result.text)
        print result_dic
        if result_dic['code'] == "0" and result_dic['msg'] == "Success":
            print u"填充快递单号成功"
        else:
            print u"填充快递单号失败"


if __name__ == "__main__":
    s = webLogin(account="qzhong", password="b123456", source="demoerp")
    if s:
        # audit(150)
        # fill_waybill(s, 19)
        batch_shipment(s, 150)
        batch_shipment(s, 200)
        batch_shipment(s, 250)
        batch_shipment(s, 300)
        batch_shipment(s, 450)
        batch_shipment(s, 500)

        # 发货150
    #     id_list = audit(150)
    #     fill_waybill(id_list)
    # audit(150)
    # id_list = [8982, ]
    # fill_waybill(id_list)
    # batch_shipment(200)
