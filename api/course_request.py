# coding=utf8
from conf import urlConfig, dataConfig
from lib import xgjRequest
from lib.built_in import *


class CourseRequest(xgjRequest.XgjRequest):

    def add_new_course(self, price, amount=0, shift_spec_money=0, shit_spec_amount=0, unit=1, is_one2one=0,
                       is_by_term=1, is_dynamic_consume=0, enable_subject=0,
                       enable_shift_spec=0, status=1, minutes2times=0, goods_list="", product_type="", auth_list=""):
        course_name = "interface_" + gen_random_string(9)
        category = self.dictionary_get("SHIFT_CAT")[0]['ID']
        grade = self.dictionary_get("SHIFT_GRADE")[0]['ID']
        term = self.dictionary_get("CLASS_TERM")[0]['ID']
        class_type = self.dictionary_get("CLASS_TYPE")[0]['ID']
        subject = self.dictionary_get("SUBJECT")[0]['ID']
        url = urlConfig.add_course + "?_ver_=" + dataConfig.js_version
        shift_schedule = []
        shift_schedule_obj = json.dumps(shift_schedule)
        course_spec = self.query_specs()[0]
        if enable_shift_spec == 1:
            shift_spec = {
                'ShiftSpecTypeID': course_spec['ID'],
                'ShiftSpecTypeName': course_spec['ID'],
                "Amount": shit_spec_amount, "Money": shift_spec_money, "primaryMoney": ""
            }
            shift_spec_auth = shift_spec.copy()
            shift_spec_auth['CampusID'] = self.campus_id

            auth_list = [
                {"ID": self.campus_id, "Name": "QTP", "UnitPrice": price,
                 "ShiftSpecList": [shift_spec_auth]}]
        else:
            auth_list = [
                {"ID": self.campus_id, "Name": "QTP", "UnitPrice": price,
                 "ShiftSpecList": []}]
        shift_spec = {}
        shift_spec_obj = json.dumps([shift_spec])
        auth_list_object = json.dumps(auth_list)
        data = {
            "ID": "",
            "Category": category,
            "GoodsList": goods_list,
            "ProductType": product_type,
            "Status": status,
            "MinutesToTimes": minutes2times,
            "IsDynamicConsume": is_dynamic_consume,
            "ShiftSpecObject": shift_spec_obj,
            "IsByTerm": is_by_term,
            "CourseAmountPerTerm": amount,
            "Term": term,
            "Name": course_name,
            "UnitPrice": price,
            "ShiftScheduleobject": shift_schedule_obj,
            "EnableShiftSpec": enable_shift_spec,
            "Grade": grade,
            "ClassType": class_type,
            "Describe": "",
            "IsOneToOne": is_one2one,
            "EnableSubject": enable_subject,
            "ConsumeAmount": 1 if unit == 3 else amount,
            "StandardMinutes": 100,
            "Year": 2018,
            "CourseTimes": 10,
            "Unit": unit,
            "Subject": subject,
            "AuthListObject": auth_list_object
        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            # 查询普通课程和按月计费课程
            is_month_unit = 1 if int(unit) == 3 else 0
            query = self.query_course(course_name, status, is_month_unit=is_month_unit)
            return query if query else False
        return False

    def query_course(self, course_name, status, is_month_unit):
        url = urlConfig.query_course
        data = {
            "Grade": 0,
            "Subject": 0,
            "Category": 0,
            "Query": course_name,
            "Year": 2018,
            "Term": 0,
            "ClassType": 0,
            "PageSize": 10,
            "PageIndex": 1,
            "TotalCount": 12,
            "PageCount": 2,
            "shiftType": 7,
            "Byauthorize": 0,
            "desc": 1,
            "sort": "CreateTime",
            "campus": self.campus_id,
            "status": status,
            "isMonthUnit": is_month_unit, }
        response = self.do_request(url, request_type="POST", **data)
        actual_is_month_unit = 1 if int(response[0]['UnitCode']) == 3 else 0
        if response[0]['Status'] == int(status) and actual_is_month_unit == is_month_unit:
            if course_name:
                return response[0] if response[0]['Name'] == course_name else False
            else:
                return response[0]
        return False

    def query_course_mini(self, course_name, status):
        url = urlConfig.query_course_mini
        data = {
            "query": course_name,
            "PageSize": 10,
            "PageIndex": 1,
            "status": status,
            "campus": self.campus_id,
            "campusid": self.campus_id,
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def delete(self, id_list):
        ids_str = ",".join(id_list)
        url = urlConfig.delete_course
        data = {
            "ids": ids_str
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_specs(self):
        response = self.dictionary_get("SHIFT_SPEC")
        return response

    def query_course_form_fields(self):
        url = urlConfig.query_course_form_fields
        data = {
            "status": 1,
            "type": 8,
            "table": "tShift",
            "campus": self.campus_id,
            "_": get_timestamp()
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_course_detail(self, course_id):
        url = urlConfig.get_course_detail
        data = {
            "id": course_id
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def modify_course(self, dic):
        url = urlConfig.modify_course + "?_ver_=" + dataConfig.js_version
        if isinstance(dic, dict):
            response = self.do_request(url, request_type="POST", **dic)
            return response
        return False

    # def export_course(self, file_name):
    #     url = urlConfig
    #     self.export_excel_file(file_name)
    #     pass

    def is_course_exist(self, course_name):
        data = {
            "id": "",
            "name": course_name,
            "_": get_timestamp()
        }


if __name__ == "__main__":
    abc = CourseRequest(session=1)
    # print company.add_new_member(37484, add_type=2)
    print "this is a test run!"
    # data = {
    #     'id': 1,
    #     'name': "abc"
    # }
    # print  [data]
