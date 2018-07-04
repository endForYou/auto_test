# coding=utf8
from conf import urlConfig, dataConfig
from lib import xgjRequest
from lib.built_in import *
from api import class_request


class ChargeRequest(xgjRequest.XgjRequest):

    def charge(self, charge_type, student=None, course_info=None, class_info=None, money=None):
        """
           student = {
               'Name': 'test',
               'ID' : 123
           }
           money = {
               'price': 1,
               'discount': 0.90,
               'amount': 20,
               'direct_reduce': 10,
               'total': 1000



           }
        """
        charge_flag_info = self.get_charge_type()
        product_type_id = self.get_product_type()[0]['ID']
        point = self.get_point_rule()[0]
        data = {
            "CampusID": self.campus_id,
            "Date": get_current_date(),
            "PaymentAccount": "",
            "Describe": "",
            "InvoiceNo": "",
            "InvoiceTitle": "",
            "CompanyTaxNo": "",
            "OpenBank": "",
            "EffectDate": get_current_date(),
            "DirectReduce": money['direct_reduce'],
            "FeeChargeDiscountList": [],
            "ChargeFlag": charge_flag_info[0]['ID'],
            "ChargeFlagNames": charge_flag_info[0]['Value'],
            "FeeEmployeeList": [],
            "FeeAccountList": [{
                "AccountID": self.get_bank_account()[0]['AccountID'],
                "Name": "现金",
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
            "ProductTypeID": product_type_id,
            "OnlineOrderID": "00000000-0000-0000-0000-000000000000",
            "FeeUpdateTime": get_current_date(fmt="%Y-%m-%d %H:%M:%S"),
            "Point": 0,
            "PointReduce": 0,
            "PointX": point['X'],
            "PointY": point['Y'],
            "ReserveMoney": 0,
            "ReserveMoneyReduce": 0,

        }

        if charge_type == "new":
            # 允许同课不同价的课程
            course_charge_info = self.get_course_charge_info(course_info['ID'])
            charge_flag_info = [x for x in charge_flag_info if x['Value'] == u"新增"]
            phone = get_random_num(1, 11)
            data['SaveType'] = 0
            data['StudentID'] = "00000000-0000-0000-0000-000000000000"
            data['StudentInfo'] = {
                "Name": student['Name'],
                "Sex": 1,
                "SMSTel": phone,
                "UserName": student['Name'] + "@release",
                "SaleModeList": [],
                "Grade": 0,
                "ClassName": "",
                "IDNumber": "",
                "Introducer": "",
                "SaleMode": ""
            }
            data['OughtPay'] = money['total']
            data['ShouldPay'] = money['total']
            data['PayFact'] = money['total']
            data['FeeAccountList'][0]['InMoney'] = money['total']
            data["OughtPayFact"] = money['total']
            data["FeeChargeList"] = [{
                "Type": 0,
                "ShiftOrGoodID": course_info['ID'],
                "UnitPrice": money['price'],
                "$TermPrice": money['price'],
                "BuyUnit": 0,
                "CourseAmount": money['amount'],
                "FreeAmount": 0,
                "StartDate": "01-01-01",
                "EndDate": "01-01-01",
                "Discount": money['discount'] * 100,
                "DiscountPrice": money['price'] * money['discount'],
                "TotalMoney": money['total'],
                "CourseAmountPerTerm": 6,
                "InReduce": 1,
                "Name": course_charge_info['Name'],
                "Unit": course_charge_info['Unit'],
                "IsByTerm": course_charge_info['IsByTerm'],
                "campusId": self.campus_id,
                "PlanList": [],
                "$campusName": "",
                "$IsOneToOne": 0,
                "DiscountID": "00000000-0000-0000-0000-000000000000",
                "DiscountName": "",
                "MustSelectSeat": False,
                "ReduceMoney": money['direct_reduce'],
                "beInputDiscount": "",
                "$discount": money['discount'] * 100,
                "IsPermit": 0,
                "OutDate": "2018-06-16",
                "ChargeFlag": charge_flag_info[0]['ID'],
                "ChargeFlagNames": charge_flag_info[0]['Value'],
                "CheckedChargeFlag": charge_flag_info[0]['ID'],
                "CheckedTypeName": charge_flag_info[0]['Value'],
                "FeeChargeShiftList": [{
                    "ClassID": class_info["ID"],
                    "ClassroomID": class_info["ClassroomID"],
                    "ClassName": class_info["Name"],
                    "nRow": 0,
                    "nCol": 0,
                    "SeatName": "",
                    "toSeat": {
                        "Flag": -1
                    },
                    "InClassDate": get_current_date(),
                    "IsExist": 0
                }],
                "checkAllBool": False,
                "selectedRow": [class_info["ID"], ],
                "ShiftSpecList": course_charge_info['ShiftSpecList'],
                "ShiftSpecID": course_charge_info['ShiftSpecList'][0]['ID'] if course_charge_info[
                    'ShiftSpecList'] else '00000000-0000-0000-0000-000000000000',
                "curSpecName": u"%s %d课时 ￥%f" % (course_charge_info['ShiftSpecList'][0]['ShiftSpecTypeName'],
                                                 course_charge_info['ShiftSpecList'][0]['Amount'],
                                                 course_charge_info['ShiftSpecList'][0]['Money']) if course_charge_info[
                    'ShiftSpecList'] else "",
                "isSelectedSpec": True,
                "primaryPrice": money['price'],
                "primaryBuyUnit": 1,
                "DiscountMoney": int(
                    (money['price'] - money['direct_reduce'] / money['amount']) * (1 - money['discount'])
                    * money['amount'])
            }]
            data["FeeChargeDiscountList"] = [
                {
                    "IsPermit": 0,
                    "DiscountID": "00000000-0000-0000-0000-000000000000",
                    "DirectReduce": money['direct_reduce']
                }
            ] if money['direct_reduce'] else []

        elif charge_type == "renew":
            charge_flag_info = [x for x in charge_flag_info if x['Value'] == u"续费"]
            if student:
                data['SaveType'] = 1
                data['StudentID'] = student['ID']
                data['StudentInfo'] = {
                    "Name": student['Name']
                }
                data['OughtPay'] = 0
                data['ShouldPay'] = 0
                data['PayFact'] = money['total']
                data['OughtPayFact'] = 0
                data['FeeAccountList'][0]['InMoney'] = money['total']
                data['FeeChargeList'] = []
                data['ChargeFlag'] = charge_flag_info[0]['ID']
                data['ChargeFlagNames'] = charge_flag_info[0]['Value']
                data['FeeUpdateTime'] = student['FeeUpdateTime']
                data['ReserveMoney'] = student['ReserveMoney']

            else:
                return False
        elif charge_type == "prestore":
            pass
        elif charge_type == "expand":
            pass
        else:
            return False
        data = json.dumps(data)
        data_dict = {
            "data": data,
            "isNew": 1
        }
        url = urlConfig.charge + "?_ver_=" + dataConfig.js_version
        response = self.do_request(url, request_type="POST", **data_dict)
        return response if response else False

    def save_order(self):
        pass

    def is_valid_coupon(self, coupon_no):
        url = urlConfig.is_valid_coupon
        data = {
            'couponNo': coupon_no,
            'campusID': self.campus_id,
            'shiftIDs': "",
            "goodIDs": "",
            'dateTime': get_current_date(),
            'chargeID': "00000000-0000-0000-0000-000000000000"
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def is_valid_invoice(self, invoice_no):
        url = urlConfig.is_valid_invoice
        data = {
            'value': invoice_no
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_bank_account(self):
        url = urlConfig.query_bank_account
        data = {
            'campusId': self.campus_id,
            'pType': 1,
            'hideWechatAndAlipay': 0
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_pos_info(self):
        url = urlConfig.query_pos_info
        data = {
            'campusId': self.campus_id,
            'pType': 1
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_charge_type(self):
        response = self.dictionary_get("FeeCustType")
        return response

    def get_product_type(self):
        response = self.dictionary_get("PRODUCT_TYPE")
        return response

    def get_charge_template(self):
        url = urlConfig
        data = {
            'campus': self.campus_id,
            '_': get_timestamp()
        }
        response = self.do_request(url, request_type="GET", **data)
        return response

    def get_student_charge_info(self, student_id):
        url = urlConfig.get_student_charge_info
        data = {
            'id': student_id,
            'campus': self.campus_id
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_course_charge_info(self, course_id, student_id=""):
        url = urlConfig.get_course_charge_info
        is_new = 0 if student_id else 1
        data = {
            'id': course_id,
            'student': student_id,
            'campus': self.campus_id,
            'isNew': is_new,
            '_': get_timestamp()
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_point_rule(self):
        url = urlConfig.point_rule
        data = {
            'code': 'reduce_Pay'
        }
        response = self.do_request(url, request_type="POST", **data)
        return response


if __name__ == "__main__":
    abc = ChargeRequest(session=1)
    # print company.add_new_member(37484, add_type=2)
    # print "this is a test run!"
    # print "%s %d课时 ￥%f" % ("hh", 50, 50.1),
    phone = get_random_num(1, 11)
    print phone
    pass
