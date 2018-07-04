# coding=utf8
from lib import xgjRequest
from conf import urlConfig, dataConfig
from lib.built_in import *
from api import class_request, course_request, charge_request, staff_request


class ReportRequest(xgjRequest.XgjRequest):
    """
    查询收费报表收据列表
    返回部门列表和员工列表
    """

    def query_charge_report_receipt_list(self, student_name, fee_type, flags="2,1,0,-1", account_id="", course_id="",
                                         course_name="", class_id="", invoice_no="", contract_no="", receipt_no="",
                                         person="", person_id="", cs_date="", ce_date="", status=-1, invalid=0,
                                         cs_effect_date="", ce_effect_date="", cs_handover_date="",
                                         ce_handover_date=""):
        url = urlConfig.query_charge_report_receipt_list
        data = {'cClassId': class_id,
                'pageSize': '10',
                'onlinePay': '',
                'saleModeId': '',
                'ceHandoverDate': ce_handover_date,
                'InvoiceNoFlag': '3',
                'ReceiptNo': receipt_no,
                'query': student_name, 'shiftName': course_name,
                'accountId': account_id,
                'Status': status,
                'InvoiceNo': invoice_no,
                'invalid': invalid, 'ContractNo': contract_no,
                'ceEffectDate': ce_effect_date,
                'flags': flags,
                'sort': 'Date', 'pageIndex': '0', 'ceDate': ce_date,
                'PersonId': person_id, 'Person': person,
                'desc': '1',
                'csEffectDate': cs_effect_date, 'cShiftId': course_id,
                'csHandoverDate': cs_handover_date,
                'cCampusId': self.campus_id, 'Describe': '', 'className': '',
                'employeeUserId': '', 'csDate': cs_date,
                'feeType': fee_type}
        response = self.do_request(url, request_type="POST", **data)
        if response:
            if student_name:
                return response['DataList'][0] if response['DataList'][0]['StudentName'] == student_name else False
            else:
                return response['DataList'][0]
        return False

    def get_charge_report_receipt_detail(self, receipt_id):
        url = urlConfig.get_charge_report_receipt_detail
        data = {
            "id": receipt_id
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def make_charge_report_receipt_invalid(self, receipt_id):

        url = urlConfig.make_charge_report_receipt_invalid + "?_ver_=" + dataConfig.js_version
        data = {
            "id": receipt_id,
            "validinvoiceno": 0
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_consume_list(self, student_name, class_id="", class_name="", status=1, s_date="", e_date="",
                                   course_id="", course_name="", shift_type=7, is_attend="", teacher_id="",
                                   master_id="", head_master_id=""):
        url = urlConfig.query_student_consume_list
        data = {'classId': class_id, 'className': class_name, 'sDate': s_date, 'shiftID': course_id, 'PageSize': '10',
                'TotalCount': '2', 'eDate': e_date, 'PageCount': '1', 'shiftType': shift_type, 'sort': 'Serial',
                'IsAttend': is_attend, 'stuStatus': status, 'flag': '', 'headMasterId': head_master_id,
                'query': student_name,
                'teacherId': teacher_id, 'campusid': self.campus_id, 'shiftName': course_name,
                'masterUserId': master_id, 'PageIndex': '1', 'desc': '1'}

        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_cost_list(self, student_name, class_id="", class_name="", status=1):
        url = urlConfig.query_student_cost_list
        data = {'classid': class_id, 'sort': 'Serial', 'pageIndex': '1',
                'campusid': self.campus_id, 'pageSize': '10', 'type': '1',
                'className': class_name, 'stuStatus': status, 'query': student_name, 'shiftName': '', 'desc': '1'}
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_cost_detail(self, student_id):
        url = urlConfig.query_student_cost_detail
        data = {'sort': 'ShiftName',
                'campusid': self.campus_id, 'type': 0,
                'cStudentUserID': student_id, 'desc': 0}
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_charge_record(self, student_id):
        url = urlConfig.query_student_charge_record
        data = {
            'campusid': self.campus_id, 'type': 0,
            'cStudentUserID': student_id, }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_cost_warning_list(self, student_name, end_date, class_name="", status=1, where_amount=">0",
                                        where_money=">0", course_name="", is_month_unit=""):
        url = urlConfig.query_student_cost_warning_list
        data = {'Category': '', 'isGroupbyProductType': '0', 'campusid': self.campus_id,
                'pageSize': '10', 'Term': '', 'stuStatus': status, 'query': student_name, 'isMonthUnit': is_month_unit,
                'shiftName': course_name,
                'studentGrade': '0', 'wheremoney': where_money, 'empList': '', 'whereamount': where_amount, 'sort': '',
                'pageIndex': '0', 'time': end_date, 'desc': '1', 'queryFlag': '1', 'Grade': '', 'masterList': '',
                'className': class_name, 'saleEmpList': '', 'Year': '', 'Subject': ''}
        response = self.do_request(url, request_type="POST", **data)
        return response

    def calculate_counselor_sign_bill_performance(self):
        url = urlConfig.calculate_sign_bill_performance
        in_data = {"startDate": "2018-03-24 00:00:00", "endDate": "2018-04-23 23:59:59", "IfAttendance": 1,
                   "IfCost": 1, "statisticalMethod": 0, "campusids": "ee0b9bd9-6fdc-4184-b31d-42a2a49867ee",
                   "EmployeeIDlist": [{"userid": "5ff405d0-626b-472a-aeaa-065cd8f14269"}], "year": 2018, "month": 4,
                   "SaleModeList": []}
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'isTotal': 0,
            'roleIDs': 'c4a8ce56-c296-47d3-bbec-eaa4acccda1b,e8fc36f3-b196-4589-864f-148c8e6836b7,c1e04699-3c39-41a8-93b7-b14ccf607692,12716806-8c63-4de4-bb43-9e60ac1aef0f,de52e7a0-7f7d-4a6c-a88b-ef9094db50cd,dfd7e4ea-d0b0-4da3-9ab6-61edb878100d,2e2e0b35-22af-456b-8c93-841eaa7e05a4,e6ec5502-49dd-4efa-9a6c-e20022876ac3,001adb17-b504-4c4d-94ef-4096fd988351,fbc455ed-6885-4c07-87c0-0d9e8f3ce578,4e68957b-4f85-430d-80b1-8ff7cfb2e618,08836a40-9cca-488e-b0f7-5cad8308c9c4,e19ab270-379d-4dbe-8aa6-89dd39cdcc41,b759b066-fbbd-446b-a62a-6525523b94f1',
            'isShift': '0,1,2',
            'PageSize': 10,
            'PageIndex': 0,
            'TotalCount': 0,
            'PageCount': 0,
            'desc': 0,
            'sort': 'Serial',
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
            'feeType': "9a0a1083-9d35-4ae6-b1ff-c2a8326ac6ad,280d5be3-2fd4-4c0e-9361-3eff2f4209e6,cf1cc554-45dc-48ca-9626-23ac996cb542,123cecff-cde6-4fea-bd65-f2abf8d45870"
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def calculate_performance(self):
        url = urlConfig.calculate_consume_performance
        in_data = {"startDate": "2018-03-24 00:00:00", "endDate": "2018-04-23 23:59:59", "IfAttendance": 1,
                   "IfCost": 1, "statisticalMethod": 0, "campusids": "ee0b9bd9-6fdc-4184-b31d-42a2a49867ee",
                   "EmployeeIDlist": [{"userid": "5ff405d0-626b-472a-aeaa-065cd8f14269"}], "year": 2018, "month": 4,
                   "SaleModeList": []}
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'isTotal': 0,
            'roleIDs': 'c4a8ce56-c296-47d3-bbec-eaa4acccda1b,e8fc36f3-b196-4589-864f-148c8e6836b7,c1e04699-3c39-41a8-93b7-b14ccf607692,12716806-8c63-4de4-bb43-9e60ac1aef0f,de52e7a0-7f7d-4a6c-a88b-ef9094db50cd,dfd7e4ea-d0b0-4da3-9ab6-61edb878100d,2e2e0b35-22af-456b-8c93-841eaa7e05a4,e6ec5502-49dd-4efa-9a6c-e20022876ac3,001adb17-b504-4c4d-94ef-4096fd988351,fbc455ed-6885-4c07-87c0-0d9e8f3ce578,4e68957b-4f85-430d-80b1-8ff7cfb2e618,08836a40-9cca-488e-b0f7-5cad8308c9c4,e19ab270-379d-4dbe-8aa6-89dd39cdcc41,b759b066-fbbd-446b-a62a-6525523b94f1',
            'isShift': '0,1,2',
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
            'feeType': "9a0a1083-9d35-4ae6-b1ff-c2a8326ac6ad,280d5be3-2fd4-4c0e-9361-3eff2f4209e6,cf1cc554-45dc-48ca-9626-23ac996cb542,123cecff-cde6-4fea-bd65-f2abf8d45870"
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def calculate_student_manage_teacher_consume_performance(self, is_total=0):
        staff_request_obj = staff_request.StaffRequest(self.session)
        charge_request_obj = charge_request.ChargeRequest(self.session)
        teacher = staff_request_obj.get_teachers()[0]
        charge_type_list = charge_request_obj.get_charge_type()
        fee_type = ",".join([x['ID'] for x in charge_type_list])
        employee_id_list = [{"userid": teacher['ID']}]
        url = urlConfig.calculate_student_manage_teacher_consume_performance
        in_data = {
            "startDate": (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") + " 00:00:00",
            "endDate": get_current_date(fmt="%Y-%m-%d") + " 23:59:59", "shiftType": 7,
            "IfAttendance": 1,
            "IfCost": 1, "statisticalMethod": 0, "campusids": "0000-0000-0000-0000-0000-0000-0000-0000",
            "EmployeeIDlist": employee_id_list,
            "year": get_current_date(fmt="%Y"), "month": get_current_date(fmt="%m"),
            "feeType": fee_type
        }
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'isTotal': is_total,
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_counselor_performance_list(self, count_type="consume", is_total=0):
        staff_request_obj = staff_request.StaffRequest(self.session)
        charge_request_obj = charge_request.ChargeRequest(self.session)
        sale_role_list = staff_request_obj.get_sale_role()
        teacher = staff_request_obj.get_teachers()[0]
        charge_type_list = charge_request_obj.get_charge_type()
        role_ids = ",".join([x['ID'] for x in sale_role_list])
        fee_type = ",".join([x['ID'] for x in charge_type_list])
        employee_id_list = [{"userid": teacher['ID']}]
        if count_type == "consume":
            url = urlConfig.query_counselor_consume_performance_list
        elif count_type == "sign":
            url = urlConfig.query_counselor_sign_bill_performance_list
        else:
            return False
        in_data = {
            "startDate": (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") + " 00:00:00",
            "endDate": get_current_date(fmt="%Y-%m-%d") + " 23:59:59", "IfAttendance": 1,
            "IfCost": 1, "statisticalMethod": 0, "campusids": self.campus_id,
            "EmployeeIDlist": employee_id_list,
            "year": get_current_date(fmt="%Y"),
            "month": get_current_date(fmt="%m"),
            "SaleModeList": []
        }
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'isTotal': is_total,
            'roleIDs': role_ids,
            'isShift': '0,1,2',
            'PageSize': 10,
            'PageIndex': 0,
            'TotalCount': 0,
            'PageCount': 0,
            'desc': 0,
            'sort': 'Serial',
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
            'feeType': fee_type
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_teacher_performance_list(self, is_total=0):
        staff_request_obj = staff_request.StaffRequest(self.session)
        teacher = staff_request_obj.get_teachers()[0]
        employee_id_list = [{"userid": teacher['ID']}]
        if is_total:
            url = urlConfig.query_teacher_consume_performance_total_list
        else:
            url = urlConfig.query_teacher_consume_performance_list
        in_data = {
            "startDate": (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") + " 00:00:00",
            "endDate": get_current_date(fmt="%Y-%m-%d") + " 23:59:59",
            "statisticalMethod": 0, "campusids": self.campus_id,
            "EmployeeIDlist": employee_id_list,
            "year": get_current_date(fmt="%Y"),
            "month": get_current_date(fmt="%m"),
            "RoleType": 1,
            "shiftType": 7
        }
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'PageSize': 10,
            'PageIndex': 0,
            'TotalCount': 0,
            'PageCount': 0,
            'desc': 0,
            'sort': 'Serial',
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_student_manage_teacher_performance_list(self, is_total=0):
        staff_request_obj = staff_request.StaffRequest(self.session)
        teacher = staff_request_obj.get_teachers()[0]
        employee_id_list = [{"userid": teacher['ID']}]
        charge_request_obj = charge_request.ChargeRequest(self.session)
        charge_type_list = charge_request_obj.get_charge_type()
        fee_type = ",".join([x['ID'] for x in charge_type_list])

        url = urlConfig.query_student_manage_teacher_performance_list
        in_data = {
            "startDate": (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") + " 00:00:00",
            "endDate": get_current_date(fmt="%Y-%m-%d") + " 23:59:59",
            "statisticalMethod": 0, "campusids": self.campus_id,
            "EmployeeIDlist": employee_id_list,
            "year": get_current_date(fmt="%Y"),
            "month": get_current_date(fmt="%m"),
            "shiftType": 7,
            "IfAttendance": 1, "IfCost": 1
        }
        in_data_json = json.dumps(in_data)
        data = {
            'data': in_data_json,
            'isTotal': is_total,
            'PageSize': 10,
            'PageIndex': 0,
            'TotalCount': 0,
            'PageCount': 0,
            'desc': 0,
            'sort': 'Serial',
            'Subject': "",
            'Year': "",
            'Term': "",
            'Grade': "",
            'Category': "",
            'feeType': fee_type
        }
        response = self.do_request(url, request_type="POST", **data)
        return response


if __name__ == "__main__":
    pass
    # ids_str = ",".join(['123', ])
    # print ids_str
