# coding=utf8
import json
from HReLib import webLogin


def approve(session):
    approve_list_url = "http://www.dayjianzhu.com/zkxx_page/project/getProjectSHList.do"
    get_approvalProcessId_url = "http://www.dayjianzhu.com/zkxx_page/project/getProjectdetai.do"
    approve_url = "http://www.dayjianzhu.com/zkxx_page/project/updateShenheproject.do"
    for index in range(1, 10):
        # 查询审批列表
        data = {
            "projectName": "",
            "provinceID": -1,
            "projectTypeId": -1,
            "projectState": 0,
            "pageIndex": 1,
            "pageSize": 50
        }
        result = session.post(approve_list_url, data)
        if result:
            # 查询processId
            approve_list = json.loads(result.text)['returnData']
            if approve_list:
                for x in range(0, len(approve_list)):
                    print approve_list
                    projectId = approve_list[x]['projectId']
                    project_data = {
                        "billType": 3,
                        "projectId": projectId
                    }
                    project_result = session.post(
                        get_approvalProcessId_url, project_data)
                    approvalProcessId = json.loads(
                        project_result.text)['returnData']['approvalProcessId']
                    # 审批
                    approve_data = {
                        "projectId": projectId,
                        "approvalProcessId": approvalProcessId,
                        "state": 1
                    }
                    approve_result = session.post(approve_url, approve_data)
                    message = json.loads(approve_result.text)['returnMessage']
                    if message == u"操作成功！":
                        print str(projectId) + u"审批成功!"


def sent_approve(session):
    to_sent_list_url = "http://www.dayjianzhu.com/zkxx_page/project/getProjectList.do"
    sent_approve_url = "http://www.dayjianzhu.com/zkxx_page/project/sendProjectCheck.do"
    for index in range(1, 51):
        to_sent_list_data = {
            "state": 1,
            "projectName": "",
            "provinceID": -1,
            "projectTypeId": -1,
            "projectState": 0,
            "pageIndex": index,
            "pageSize": 50
        }
        result = session.post(to_sent_list_url, to_sent_list_data)
        if result:
            to_sent_result = json.loads(result.text)['returnData']
            if to_sent_result:
                for x in range(0, len(to_sent_result)):
                    projectId = to_sent_result[x]['projectId']
                    sent_approve_data = {
                        "projectId": projectId,
                    }
                    sent_approve_result = session.post(
                        sent_approve_url, sent_approve_data)
                    message = json.loads(
                        sent_approve_result.text)['returnMessage']
                    if message == u"操作成功！":
                        print str(projectId) + u"送审成功!"


def certificateBorrow(session):
    url = "http://www.dayjianzhu.com/zkxx_page/certificate/insertCertificateBorrow.do"
    data = {
        "orgId": 212,
        "borrowUse": 3,
        "projectId": 50171742,
        "projectName": "testproject17410",
        "useDate": "2017-10-11",
        "expectReturnDate": "2017-10-25",
        "applyReason": "测试借出归还",
        "borrowStatus": 2,
        "certificateIds": "[3521405]"
    }
    borrow_result = session.post(url, data)
    message = json.loads(borrow_result.text)['returnMessage']
    if message == u"操作成功！":
        print u"申请成功!"


session1 = webLogin.webLogin("18511183830", "b123456", source="dayjz")
for x in range(0, 9999):
    certificateBorrow(session1)
# sent_approve(session1)


# session2 = webLogin.webLogin("18511183831", "b123456", source="dayjz")
# approve(session2)
# session3 = webLogin.webLogin("18511183866", "b123456", source="dayjz")
# approve(session3)
# session4 = webLogin.webLogin("18511183835", "b123456", source="dayjz")
# approve(session4)
