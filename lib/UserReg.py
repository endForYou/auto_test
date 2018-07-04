# coding=utf8

from HReLib import regCompany
import random
import json
from HReLib.hreUser import HreUser

# 注册
for i in range(1, 2):
    mobile = "185" + str(random.randint(10000000, 99999999))
    print regCompany.companyReg("qiye"+str(i), "b123456", "qiye53"+str(i) , mobile,source="dayHRe")

# for i in range(51, 101):
#     mobile = "181" + str(random.randint(10000000, 99999999))
#     print regCompany.companyReg("supplier" + str(i), "b123456", "supplier" + str(i), mobile,
#                                 "http://hre.daydao.com/dayhro/DayhroLogin/login.do")
# 授权
# for i in range(51, 101):
#     s = HreUser("supplier" + str(i), role=4)
#     uuid = s.get_operator_id()
#     print s.modify_operator(uuid, "supplier" + str(i), "2,3,4")

# 签订协议
# for i in range(51, 101):
#     company_manager = HreUser("qiye" + str(i), role=1)
#     company_corp_id = company_manager.get_corp_id()
#     company_corp_name = company_manager.get_corp_name()
#
#     receptionist_manager = HreUser("supplier" + str(i), role=4)
#     receptionist_corp_id = receptionist_manager.get_corp_id()
#     receptionist_corp_name = receptionist_manager.get_corp_name()
#     receptionist_id = receptionist_manager.get_receptionists_list("supplier" + str(i))[
#         0]['uuid']
#
#     receptionist_name = receptionist_manager.get_receptionists_list("supplier" + str(i))[
#         0]['operatorName']
#     agreement_list = receptionist_manager.get_supplier_agreement_list(
#         1, company_corp_name)
#     # 确保是找到正确的协议记录
#     agreement = [
#         x for x in agreement_list if str(
#             x['auditee']) == company_corp_id][0]
#     # 取得刚才添加记录的uuid
#     agreement_uuid = agreement['uuid']
#     print company_manager.confirm_agreement(agreement_uuid)
#     # 添加增员
#     agreement_dict = {
#         "uuid": "",
#         "agreeProducts": [
#             {
#                 "show": "true",
#                 "insuredPlace": "471",
#                 "insuredPlaceName": "南京",
#                 "productId": 296,
#                 "productName": "人事代理",
#                 "billServiceDate": 735,
#                 "billServiceDateName": "当月投当月",
#                 "price": "222",
#                 "isNew": "true"}],
#         "client": receptionist_corp_id,
#         "clientName": receptionist_corp_name,
#         "orderConfirmDays": "2",
#         "orderReceiveDay": "2",
#         "servicerId": receptionist_id,
#         "auditee": company_corp_id,
#         "auditeeName": company_corp_name,
#         "servicerName": receptionist_name}
#     agreementJsonStr = json.dumps(agreement_dict)
#     print receptionist_manager.add_agreement(agreementJsonStr)

# 获取接单方uuid
# for i in range(51, 101):
#     user1 = "qiye"+str(i)
#     user = "supplier" + str(i)
#     s = HreUser(user, role=4)
#     client_uuid = s.get_corp_id()
#     print user1+","+user+","+client_uuid