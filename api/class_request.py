# coding=utf8
from lib import xgjRequest
from conf import urlConfig, dataConfig
from lib.built_in import *


class ClassRequest(xgjRequest.XgjRequest):

    def add_new_class(self, course, open_date, enable_subject=True,
                      headmaster_id="", is_send_course_msg=1, check_conflict=0, is_skip_holiday=1, is_seat_classroom=0):
        class_name = "interface_" + gen_random_string(9) + str(random.randint(1, 20)) + u"班"
        term = self.dictionary_get("CLASS_TERM")[0]['ID']
        url = urlConfig.add_class + "?_ver_=" + dataConfig.js_version
        data = {
            "ID": "00000000-0000-0000-0000-000000000000",
            "Name": class_name,
            "MaxStudentsAmount": "15",
            "OpenDate": open_date,
            "FinishedDate": "1900-01-01",
            "ClassroomID": "00000000-0000-0000-0000-000000000000",
            "ClassroomName": "",
            "Describe": "11",
            "CampusID": self.campus_id,
            "CloseDate": "2018-04-15",
            "CourseTimes": "22",
            "ShiftID": course['ID'],
            "Term": term,
            "Year": "2021",
            "IsSeatClassRoom": is_seat_classroom,
            "ValidAttendanceMinutes": 0,
            "Tag": "",
            "HeadMasterUserID": "00000000-0000-0000-0000-000000000000",
            "BuildCourse": 0,
            "IsSendCourseMsg": is_send_course_msg,
            "UnitCode": course['UnitCode'],
            "CheckConflict": check_conflict,
            "ConsumeAmount": 2,
            "Teachers": [
                {"ID": "00000000-0000-0000-0000-000000000000", "Role": 1, "TeacherCommissionIDs": "",
                 "SubjectID": "00000000-0000-0000-0000-000000000000"}], "Plan": [], "Commission": [],
            "IsSkipHoliday": is_skip_holiday,
            "holidays": [],
            "EnableSubject": enable_subject
        }
        data = json.dumps(data)
        data_dict = {
            "data": data
        }
        response = self.do_request(url, request_type="POST", **data_dict)
        if response:
            class_id = response['NewID']
            is_month_unit = 1 if int(course['UnitCode']) == 3 else 0
            query = self.query_class(class_name, is_month_unit=is_month_unit, finished=0,
                                     class_online_filter=0, shift_type=7)

            return query if query['ID'] == class_id else False
        return False

    def query_class(self, class_name, is_month_unit=0, finished=0, class_online_filter=0, shift_type=7, is_single=0,
                    sdate="", edate="", s_close_date="", e_close_date="", s_course_date="", e_course_date="", year="",
                    teacher_name="", teacher_id="", headmaster_name="", headmaster_id="", student_id="",
                    classroom_id="", count_courses=1, count_students=1, types=""):
        url = urlConfig.query_class
        data = {
            "Grade": " 0",
            "Subject": "0",
            "Category": "0",
            "Shift": "",
            "shiftName": "",
            "Query": class_name,
            "sdate": sdate,
            "edate": edate,
            "sCloseDate": s_close_date,
            "eCloseDate": e_close_date,
            "sCourseDate": s_course_date,
            "eCourseDate": e_course_date,
            "Year": year,
            "Term": "",
            "teacherName": teacher_name,
            "teacherId": teacher_id,
            "headMasterName": headmaster_name,
            "headMasterId": headmaster_id,
            "studentId": student_id,
            "classroomID": classroom_id,
            "isSingle": is_single,
            "weekday": "",
            "PageSize": "10",
            "PageIndex": "1",
            "TotalCount": "106",
            "PageCount": "11",
            "isMonthUnit": is_month_unit,
            "finished": finished,
            "classOnlineFilter": class_online_filter,
            "desc": "1",
            "sort": "CreateTime",
            "campus": self.campus_id,
            "countCourses": count_courses,
            "countStudents": count_students,
            "shiftType": shift_type,
            "type": types,
        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            if class_name:
                if response[0]['Name'] == class_name and response[0]['IsFinished'] == finished:
                    return response[0]
            else:
                if response[0]['IsFinished'] == finished:
                    return response[0]
        return False

    def delete(self, id_list):
        if isinstance(id_list, dict):
            id_list = ",".join(id_list)
        url = urlConfig.delete_class + "?_ver_=" + dataConfig.js_version
        data = {
            "ids": id_list
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def query_class_by_course(self, student_id, course_id):
        url = urlConfig.query_class_by_course
        data = {
            'studentid': student_id,
            'shift': course_id,
            'campus': self.campus_id,
            'pagesize': 1000
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def is_student_in_class(self, student_id, class_id):
        url = urlConfig.is_student_in_class
        data = {
            'studentId': student_id,
            'classId': class_id
        }
        response = self.do_request(url, request_type="POST", **data)
        if response['ClassList'][0]['ClassID'] == class_id and response['ClassList'][0]['IsExist'] == 1:
            return True
        return False

    def remove_student_from_class(self, class_id, student_id, out_date, out_reason=""):
        url = urlConfig.remove_student_from_class + "?_ver_=" + dataConfig.js_version
        data = {
            'id': class_id,
            'students': student_id,
            'outDate': out_date,
            'outReason': out_reason
        }
        response = self.do_request(url, request_type="POST", **data)
        # NewClassName
        return response

    def add_student_into_class(self, class_id, student_id, in_date, in_reason=""):
        url = urlConfig.add_student_into_class + "?_ver_=" + dataConfig.js_version
        data = {
            'id': class_id,
            'students': student_id,
            'indate': in_date,
            'outReason': in_reason
        }
        response = self.do_request(url, request_type="POST", **data)
        # NewClassName
        return response


if __name__ == "__main__":
    pass
    # ids_str = ",".join(['123', ])
    # print ids_str
