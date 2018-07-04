# coding=utf8
from decimal import Decimal
from functools import wraps
import xlrd
import random
from built_in import *
import json
import os
from datetime import datetime
import time
from conf import dataConfig, urlConfig

BASE_URL = dataConfig.base_url


def request_response(func):
    @wraps(func)
    def wrapper(*args, **kv):
        response = func(*args, **kv)
        # 返回布尔值说明请求失败
        if isinstance(response, bool) or response.status_code != 200:
            return False
        if isinstance(response.text, str) or isinstance(response.text, unicode):
            response = json.loads(response.text)
            if isinstance(response, dict):
                if response.get('ErrorCode') == 200:
                    if response.get('Data') is not None:
                        return response.get('Data')
                    return True
        return False

    return wrapper


class XgjRequest(object):

    def __init__(self, session):
        self.session = session
        self.campus_id = dataConfig.campus_id

    @request_response
    def do_request(self, url, request_type="POST", data_json=None, **data):
        url = BASE_URL + url
        if self.session:
            if request_type.upper() == "POST":
                if data_json:
                    response = self.session.post(url, json=data_json)
                else:
                    response = self.session.post(url, data=data)
            else:
                response = self.session.get(url, params=data)

            return response
        return False

    def import_excel_file(self, file_name, url, **data):
        attachment = {"file": open(file_name, "rb")}
        url = BASE_URL + url
        response = self.session.post(
            url, files=attachment, data=data)
        response_dic = json.loads(
            response.text)
        if response_dic['result'] == 'true' and response_dic['statusCode'] == '0':
            if response_dic.get('beans'):
                return response_dic['beans']
            else:
                return True
        return False

    def export_excel_file(self, file_name, url, **data):
        if os.path.exists(file_name):
            os.remove(file_name)
        url = BASE_URL + url
        response = self.session.get(url, stream=True, params=data)
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return file_name if response.status_code == 200 else False

    def dictionary_get(self, info_type):
        if info_type not in ["SUBJECT", "SHIFT_CAT", "SHIFT_GRADE", "CLASS_TERM", "CLASS_TYPE", "FeeCustType",
                             "PRODUCT_TYPE", "SHIFT_SPEC", "ABSENT_CAUSE", "SALE_ROLE"]:
            return False
        url = urlConfig.dictionary_get
        data = {
            'type': info_type,
            'campus': self.campus_id,
            '_': get_timestamp()
        }
        response = self.do_request(url, request_type="GET", **data)
        return response

    def get_classrooms(self):
        url = urlConfig.query_classroom
        data = {
            'campusId': self.campus_id,
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_teachers(self):
        url = urlConfig.query_staff
        data = {
            'isuser': 0,
            'isContainOut': 1,
            'campus': self.campus_id,
            '_': get_timestamp()
        }
        response = self.do_request(url, request_type="GET", **data)['EmployeeList']
        return response

    def query_sys_config(self):
        url = urlConfig.sys_config
        data = {
            'campusID': "",
            'type': 0
        }
        response = self.do_request(url, request_type="GET", **data)
        return response

    def get_sale_mode(self):
        pass


if __name__ == "__main__":
    # company = HreRequest('qiye')   # 初始化企业用户
    # print company.add_new_member(37484, add_type=2)
    print "this is a test run!"
    pass
    dic1 = {
        "SaveType": 1,
        "StudentID": "e25f40c9-f278-4ac3-b2d8-a77f49d02c51",
        "CampusID": "ee0b9bd9-6fdc-4184-b31d-42a2a49867ee",
        "StudentInfo": {
            "Name": "studentP5QB1wu33"
        },
        "Date": "2018-04-16",
        "PaymentAccount": "",
        "Describe": "",
        "InvoiceNo": "",
        "InvoiceTitle": "",
        "CompanyTaxNo": "",
        "OpenBank": "",
        "EffectDate": "2018-04-16",
        "FeeChargeList": [],
        "DirectReduce": 0,
        "FeeChargeDiscountList": [],
        "OughtPay": 0,
        "ShouldPay": 0,
        "PayFact": 2,
        "ChargeFlag": "280d5be3-2fd4-4c0e-9361-3eff2f4209e6",
        "ChargeFlagNames": "续费",
        "FeeEmployeeList": [],
        "FeeAccountList": [{
            "AccountID": "0276e5d8-85cb-4cd2-8600-fdda8a102516",
            "Name": "现金",
            "InMoney": 2,
            "DefaultCharge": 1,
            "Type": 1,
            "Pinyin": "XJ",
            "IsAllCampus": 0,
            "flag": True,
            "nameLen": 4,
            "PaymentAccount": "",
            "posList": [],
            "PosId": "00000000-0000-0000-0000-000000000000",
            "online": False
        }],
        "DiscountCalcRule": 1,
        "CouponReduce": 0,
        "FeeCouponSubList": [],
        "EnableConsumeCoupon": "0",
        "ChargeOnlineID": "00000000-0000-0000-0000-000000000000",
        "ProductTypeID": "34217226-4bbd-4086-9ffe-2dc82b83272a",
        "OnlineOrderID": "00000000-0000-0000-0000-000000000000",
        "FeeUpdateTime": "2018-04-16 17:50:47.893",
        "Point": 0,
        "PointReduce": 0,
        "PointX": 3,
        "PointY": 10,
        "ReserveMoney": 215,
        "ReserveMoneyReduce": 0,
        "OughtPayFact": 0
    }

    dcit2 = {
        "ChargeOnlineID": "00000000-0000-0000-0000-000000000000",
        "StudentID": "e25f40c9-f278-4ac3-b2d8-a77f49d02c51",
        "OughtPay": 0,
        "DirectReduce": 0,
        "ReserveMoney": 215,
        "EffectDate": "2018-04-16",
        "ChargeFlag": "280d5be3-2fd4-4c0e-9361-3eff2f4209e6",
        "DiscountCalcRule": 1,
        "PointY": 10,
        "OughtPayFact": 0,
        "CampusID": "ee0b9bd9-6fdc-4184-b31d-42a2a49867ee",
        "PaymentAccount": "",
        "FeeChargeList": [],
        "FeeChargeDiscountList": [],
        "ReserveMoneyReduce": 0,
        "InvoiceTitle": "",
        "PointReduce": 0,
        "FeeCouponSubList": [],
        "InvoiceNo": "",
        "Date": "2018-04-16",
        "PayFact": 2,
        "EnableConsumeCoupon": "0",
        "FeeAccountList": [{
            "Name": "现金",
            "nameLen": 4,
            "flag": True,
            "posList": [],
            "Type": 1,
            "DefaultCharge": 1,
            "AccountID": "0276e5d8-85cb-4cd2-8600-fdda8a102516",
            "InMoney": 2,
            "IsAllCampus": 0,
            "PaymentAccount": "",
            "PosId": "00000000-0000-0000-0000-000000000000",
            "Pinyin": "XJ",
            "online": False
        }],
        "CouponReduce": 0,
        "ProductTypeID": "34217226-4bbd-4086-9ffe-2dc82b83272a",
        "FeeEmployeeList": [],
        "FeeUpdateTime": "2018-04-16 18:04:46",
        "Point": 0,
        "ChargeFlagNames": "续费",
        "Describe": "",
        "SaveType": 1,
        "ShouldPay": 0,
        "StudentInfo": {
            "Name": "studentP5QB1wu33"
        },
        "PointX": 3,
        "CompanyTaxNo": "",
        "OpenBank": "",
        "OnlineOrderID": "00000000-0000-0000-0000-000000000000"
    }
    print cmp(dic1, dcit2)
