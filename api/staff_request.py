# coding=utf8
from lib import xgjRequest
from conf import urlConfig, dataConfig
from lib.built_in import *
from api import class_request, course_request


class StaffRequest(xgjRequest.XgjRequest):
    """
    查询员工列表
    返回部门列表和员工列表
    """

    def query_staff(self, student_name, flag=0, status=1, student_type=1, is_gross_campus=1):
        url = urlConfig.query_staff
        data = {
            'isuser': 0,
            'isContainOut': 1,
            'campus': self.campus_id,
            '_': get_timestamp()

        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            if student_name:
                return response[0]['ID'] if response[0]['Name'] == student_name else False
            else:
                return response[0]['ID'], response[0]['Name']
        return False

    def query_teacher_commission_setting(self):
        url = urlConfig.query_teacher_commission_setting
        response = self.do_request(url, request_type="POST")
        return response

    def get_sale_role(self):
        response = self.dictionary_get('SALE_ROLE')
        return response

    def get_staff_position(self):
        response = self.dictionary_get('EMP_POSITION')
        return response

    def delete(self, id_list):
        if isinstance(id_list, dict):
            id_list = ",".join(id_list)
        url = urlConfig.delete_class + "?_ver_=" + dataConfig.js_version
        data = {
            "ids": id_list
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_brief(self, student_name, status=1):
        url = urlConfig.query_student_brief
        data = {
            "campusFlag": 0,
            "shiftId": "",
            "classId": "",
            "indate1": "",
            "indate2": "",
            "status": status,
            "query": student_name,
            "className": "",
            "shiftName": "",
            "signStatus": "-1",
            "campusid": self.campus_id,
            "masterIdFlag": 0,
            "masterUserId": "",
            "sort": "Name",
            "desc": "0",
            "grade": "0",
            "school": "",
            "isSingle": "0",
            "PageSize": "10",
            "PageIndex": "0",
            "TotalCount": "0",
            "PageCount": "0",

        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            if student_name:
                return response[0]['ID'] if response[0]['Name'] == student_name else False
            else:
                return response[0]['ID'], response[0]['Name']
        return False

    def is_student_exist(self, name, phone):
        url = urlConfig.is_student_exist
        data = {
            'query': name,
            'tel': phone
        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            if response[0]['Name'] == name and response[0]['SMSTel'] == phone:
                return True
        return False

    def student_from_where(self):
        url = urlConfig.get_student_charge_info
        data = {
            'showAll': False,
        }
        response = self.do_request(url, request_type="POST", **data)
        return response


if __name__ == "__main__":
    pass
    # ids_str = ",".join(['123', ])
    # print ids_str
