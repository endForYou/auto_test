# coding=utf8
from lib import xgjRequest
from conf import urlConfig, dataConfig
from lib.built_in import *


class ArrangeLessonRequest(xgjRequest.XgjRequest):

    def arrange_normal_lesson(self, class_info, start_date, end_date, check_conflict=0, per_duration=0.5):
        classroom = self.get_classrooms()[0]
        teacher = self.get_teachers()[0]
        subject = self.dictionary_get("SUBJECT")[0]['ID']
        url = urlConfig.arrange_normal_lesson + "?_ver_=" + dataConfig.js_version
        start_time_str = "13:00"
        start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
        delta = datetime.timedelta(minutes=per_duration * 60)
        end_time = start_time + delta
        end_time_str = end_time.strftime('%H:%M')
        data = {"PlanID": "00000000-0000-0000-0000-000000000000",
                "ClassID": class_info['ID'],
                "StartDate": start_date,
                "EndDate": end_date,
                "Times": "68",
                "CheckConflict": check_conflict,
                "SubjectID": subject,
                "Teachers": [{"ID": teacher['ID'], "TeacherCommissionIDs": "", "Role": 1}],
                "Plan": [
                    {"Weekday": 1, "WeekName": "星期一", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 2, "WeekName": "星期二", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 3, "WeekName": "星期三", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 4, "WeekName": "星期四", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 5, "WeekName": "星期五", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 6, "WeekName": "星期六", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40},
                    {"Weekday": 7, "WeekName": "星期天", "StartTime": start_time_str, "EndTime": end_time_str,
                     "ClassroomID": classroom['ID'], "ClassroomName": classroom['Name'],
                     "interval": 40}
                ]
                }

        data = json.dumps(data)
        data_dict = {
            "holiday": 0,
            "data": data
        }
        response = self.do_request(url, request_type="POST", **data_dict)
        if response:
            # print response
            query = self.query_lesson(start_date, end_date, teacher=teacher['ID'], class_name=class_info['Name'])
            return query if query else False
        return False

    def query_lesson(self, start_date, end_date, teacher="", class_name=""):
        url = urlConfig.query_lesson
        data = {
            "Grade": "0",
            "Subject": "0",
            "Category": "0",
            "startDate": start_date,
            "endDate": end_date,
            "teacher": teacher,
            "shiftName": "",
            "className": class_name,
            "classroom": "",
            "studentId": "",
            "headMasterName": "",
            "headMasterId": "",
            "masters": "",
            "Year": "",
            "Term": "",
            "ClassType": "0",
            "PageSize": "10",
            "PageIndex": "1",
            "TotalCount": "1",
            "PageCount": "1",
            "desc": "0",
            "sort": "StartTime",
            "campus": self.campus_id,
            "Forenoon": "1",
            "Afternoon": "1",
            "Nightnoon": "1",
            "classId": "",
            "finished": "-1",
            "shiftType": "7",
            "IsContainFinished": " 0",
            "courseFlag": " ",

        }
        response = self.do_request(url, request_type="POST", **data)
        if response:
            return response[0]
        return False

    def delete_lesson(self, id_list):
        if isinstance(id_list, dict):
            id_list = ",".join(id_list)
        url = urlConfig.delete_class + "?_ver_=" + dataConfig.js_version
        data = {
            "ids": id_list
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def attend_class_and_call_the_roll(self, student_info, arrange_lesson_id, is_attend=1, is_cost=1,
                                       absent_cause_id=""):
        lesson_info = self.get_lesson_info(arrange_lesson_id)
        date = lesson_info['StartTime'].split("T")[0]
        last_class_time = date + "00:00-23:59[" + get_week_day(date) + "]"
        url = urlConfig.call_the_roll + "?_ver_=" + dataConfig.js_version
        data = {
            "Students": [
                {"ID": student_info['ID'], "Name": student_info['Name'], "Sex": student_info['Sex'],
                 "SMSTel": student_info['SMSTel'],
                 "IsTry": 0, "IsAttend": is_attend, "IsCost": is_cost, "IsMend": 0, "AbsentCauseID": absent_cause_id,
                 "AbsentCauseName": "",
                 "Describe": student_info['Describe'], "IsConfirmed": 0, "AdjustFlag": 0, "IsAttendStauts": 0,
                 "Photo": student_info['Photo'],
                 "RemainAmount": student_info['RemainAmount'], "OutAmount": student_info['OutAmount'],
                 "machineChecked": False
                 }
            ],
            "CourseID": arrange_lesson_id, "Describe": "", "Content": "", "shiftAmount": 0,
            "ShiftScheduleID": "00000000-0000-0000-0000-000000000000",
            "UpdateTime": student_info['UpdateTime'],
            "Action": 1, "Weixin": 1,
            "LastClasstime": last_class_time, "ComeFrom": 1, "Agnet": 0}
        data = json.dumps(data)
        data_dict = {
            "data": data
        }
        response = self.do_request(url, request_type="POST", **data_dict)
        return response

    def get_attendance(self, arrange_lesson_id):
        data = {
            "id": arrange_lesson_id
        }
        url = urlConfig.get_attendance
        response = self.do_request(url, request_type="POST", **data)
        return response

    def cancel_attend_class(self, arrange_lesson_id):
        lesson_info = self.get_lesson_info(arrange_lesson_id)
        date = lesson_info['StartTime'].split("T")[0]
        last_class_time = date + "00:00-23:59[" + get_week_day(date) + "]"
        url = urlConfig.call_the_roll + "?_ver_=" + dataConfig.js_version
        data = {
            "Students": [],
            "CourseID": arrange_lesson_id,
            "Action": -1,
            "LastClasstime": last_class_time
        }
        data = json.dumps(data)
        data_dict = {
            "holiday": 0,
            "data": data
        }
        response = self.do_request(url, request_type="POST", **data_dict)
        return response

    def get_lesson_info(self, arrange_lesson_id):
        url = urlConfig.get_lesson_info
        data = {
            "id": arrange_lesson_id
        }
        response = self.do_request(url, request_type="POST", **data)
        return response

    def get_absent_cause(self):
        response = self.dictionary_get("ABSENT_CAUSE")
        return response


if __name__ == "__main__":
    pass
    # ids_str = ",".join(['123', ])
    # print ids_str
