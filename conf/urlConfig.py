# coding=utf8
__author__ = 'Administrator'

login = "/api/login/login"
dictionary_get = "/api/Dictionary/Get"

'''
课程相关
'''
add_course = "/api/Shift/Post"
query_course = "/api/Shift/Query"
query_course_mini = "/api/shift/query"
get_course_detail = "/api/Shift/Get"
query_course_form_fields = "/api/CustomerForm/QueryCustomerForm"
modify_course = "/api/Shift/Put"
delete_course = "/api/shift/Delete"
is_course_exist = "/api/Shift/exists"
'''
班级相关
'''
add_class = "/api/Class/Post"
query_class = "/api/Class/Query"
delete_class = "/api/class/Delete"
query_class_by_course = "/api/Class/querypro"
is_student_in_class = "/api/student/IsInClass"
remove_student_from_class = "/api/Class/RemoveStudent"
add_student_into_class = "/api/Class/AddStudent"
'''
排课相关
'''
arrange_normal_lesson = "/api/Course/AddBatch"
query_lesson = "/api/Course/Query"
get_lesson_info = "/api/course/get"
delete_lesson = "/api/Course/Delete"
get_attendance = "/api/Course/GetAttendance"
call_the_roll = "/api/Course/SetAttendance"
'''
教室相关
'''
query_classroom = "/api/Classroom/Query"

'''
员工相关
'''
query_staff = "/api/depart/QueryWithEmployeeRight"
query_teacher_commission_setting = "/api/Class/QueryTeacherCommissionSetting"

'''
学生相关
'''
delete_student = "/api/Student/Delete"
query_student_brief = "/api/Student/QueryBrief"
query_student = "/api/Student/Query"
is_student_exist = "/api/Student/QuerySameNames"
student_from_where = "/api/Dictionary/SelectSaleMode"

'''
银行账户相关
'''
query_bank_account = "/api/feecharge/GetAccount"
query_pos_info = "/api/FeeCharge/GetPosInfo"

'''
收费相关
'''
charge = "/api/FeeCharge/Post"
is_valid_coupon = "/api/FeeCharge/IsValidCoupon"
is_valid_invoice = "/api/feecharge/IsValidInvoice"
get_student_charge_info = "/api/FeeCharge/get"
get_course_charge_info = "/api/FeeCharge/GetShift"
point_rule = "/api/Point/Get"

'''
报表相关
'''
# 收费报表
get_charge_report_receipt_detail = "/api/FeeChargeQuery/get"
query_charge_report_receipt_list = "/api/FeeChargeQuery/query"
make_charge_report_receipt_invalid = "/api/FeeChargeQuery/InvalidReceipt"
# 课消报表
query_student_consume_list = "/api/report/QueryReportConsumeDetail"
query_student_cost_list = "/api/Report/CourseConsume"
query_student_cost_detail = "/api/Report/CourseConsume_Student"
query_student_charge_record = "/api/Report/CourseConsume_Charge"
query_student_cost_warning_list = "/api/Report/FeeStudentShiftRemainLst"
query_counselor_consume_performance_list = "/api/report/QueryCalcSaleConsume"
query_counselor_sign_bill_performance_list = "/api/report/QueryCalcSaleSign"
query_teacher_consume_performance_list = "/api/report/QueryEmployeeConsume"
query_teacher_consume_performance_total_list = "/api/report/GetEmployeeConsumeIsTotal"
query_student_manage_teacher_performance_list = "/api/report/QueryCalcMasterConsume"
calculate_sign_bill_performance = "/api/report/CalcSaleSign"
calculate_counselor_consume_performance = "/api/report/CalcSaleConsume"
calculate_teacher_consume_performance = "/api/report/CalcTeacherConsume"
calculate_student_manage_teacher_consume_performance = "/api/report/CalcMasterConsume"

sys_config = "/api/sysConfig/query"
