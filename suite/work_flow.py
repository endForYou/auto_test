# coding=utf8
from lib.built_in import *


def charge_new(money, course_request_obj, class_request_obj, charge_request_obj, report_request_obj):
    """
    新用户报读班级收费、查看收据流程
    :param charge_request_obj:
    :param report_request_obj:
    :param money
    :param course_request_obj
    :param class_request_obj
    :return:
    """
    course = course_request_obj.add_new_course(money['price'], money['amount'], unit=money['unit'])
    class_info = class_request_obj.add_new_class(course, open_date=get_current_date())
    student_name = "student" + gen_random_string(6)
    student = {
        'Name': student_name
    }

    charge_result = charge_request_obj.charge(money=money, charge_type='new', class_info=class_info, course_info=course,
                                              student=student)
    if charge_result:
        charge_type_list = charge_request_obj.get_charge_type()
        charge_type_id_list = [x['ID'] for x in charge_type_list]
        fee_type = ",".join(charge_type_id_list)
        charge_info = report_request_obj.query_charge_report_receipt_list(student['Name'], fee_type)
        charge_id = charge_info['ChargeID']
        charge_receipt_detail = report_request_obj.get_charge_report_receipt_detail(charge_id)
        # 入账金额与总金额一致、
        if charge_receipt_detail['AccountList'][0]['InMoney'] == money['total'] and \
                charge_receipt_detail['ModeList'][0]['InMoney'] and charge_receipt_detail['PayFactDetail']['Cash']:
            return student_name
        else:
            return False
    return False


def arrange_lesson_and_call_the_roll(student_info, class_request_obj, arrange_lesson_request_obj, report_request_obj,
                                     per_duration, where_amount, where_money):
    """
    学生已报读班级，出班、入班、排课、点名上课、查看课消
    :param report_request_obj
    :param student_info:
    :param class_request_obj:
    :param arrange_lesson_request_obj:
    :param per_duration
    :param where_amount
    :param where_money
    :return:
    """
    class_info = class_request_obj.query_class(class_name="", student_id=student_info['ID'])
    is_in = class_request_obj.is_student_in_class(student_info['ID'], class_info['ID'])
    if is_in:
        # 出班
        remove_response = class_request_obj.remove_student_from_class(class_info['ID'], student_info['ID'],
                                                                      out_date=get_current_date())
        is_in = class_request_obj.is_student_in_class(student_info['ID'], class_info['ID'])
        if remove_response and not is_in:
            # 入班
            add_in_response = class_request_obj.add_student_into_class(class_info['ID'], student_info['ID'],
                                                                       in_date=get_current_date())
            is_in = class_request_obj.is_student_in_class(student_info['ID'], class_info['ID'])
            if add_in_response and is_in:
                # 排课
                arrange_response = arrange_lesson_request_obj.arrange_normal_lesson(class_info=class_info,
                                                                                    start_date=get_current_date(),
                                                                                    end_date=get_current_date(),
                                                                                    per_duration=per_duration)
                lesson_info = arrange_lesson_request_obj.query_lesson(start_date=get_current_date(),
                                                                      end_date=get_current_date(),
                                                                      class_name=class_info['Name'])
                if arrange_response and lesson_info:
                    # 点名
                    attendance_info = arrange_lesson_request_obj.get_attendance(lesson_info['ID'])
                    student_info_more = attendance_info['students'][0]
                    student_info_more['UpdateTime'] = attendance_info['updateTime']
                    call_the_roll_response = arrange_lesson_request_obj.attend_class_and_call_the_roll(
                        student_info_more,
                        lesson_info['ID'], is_cost=per_duration * 60)
                    # 查询报表
                    if call_the_roll_response:
                        student_consume = report_request_obj.query_student_consume_list(student_info['Name'],
                                                                                        class_name=class_info[
                                                                                            'Name'],
                                                                                        class_id=class_info['ID'])
                        amount_str = student_consume['data'][0]['Amount']
                        m = re.search(r'\d*\.*\d*', amount_str)
                        amount = m.group(0)
                        student_cost = report_request_obj.query_student_cost_list(student_info['Name'],
                                                                                  class_name=class_info['Name'],
                                                                                  class_id=class_info['ID'])
                        student_cost_consume_money = student_cost[0]['CourseMoney']
                        student_cost_remain_money = student_cost[0]['RemainMoney']
                        student_cost_detail = report_request_obj.query_student_cost_detail(student_info['ID'])
                        student_cost_detail_all_amount = student_cost_detail[0]['ShiftBuyAmount']
                        student_cost_detail_consume_amount = student_cost_detail[0]['ShiftConsumeAmount']
                        student_cost_detail_consume_money = student_cost_detail[0]['ShiftConsumeMoney']
                        student_cost_detail_remain_amount = student_cost_detail[0]['ShiftRemainAmount']
                        student_cost_detail_remain_money = student_cost_detail[0]['ShiftRemainMoney']
                        # student_charge_record = report_request_obj.query_student_charge_record(
                        #     student_info['ID'])
                        student_cost_warning = report_request_obj.query_student_cost_warning_list(student_info['Name'],
                                                                                                  end_date=get_current_date(),
                                                                                                  class_name=class_info[
                                                                                                      'Name'],
                                                                                                  where_amount=where_amount,
                                                                                                  where_money=where_money)
                        student_cost_warning_remain_amount = student_cost_warning['FeeStudentLessLst'][0][
                            'RemainAmount']
                        student_cost_warning_remain_money = student_cost_warning['FeeStudentLessLst'][0]['RemainMoney']
                        # print float(amount), float(student_cost_detail_consume_amount), float(amount) == float(
                        #     student_cost_detail_consume_amount)
                        # print float(student_cost_consume_money) == float(student_cost_detail_consume_money)
                        # print float(student_cost_remain_money), float(student_cost_detail_remain_money), float(
                        #     student_cost_warning_remain_money), float(student_cost_remain_money) == float(
                        #     student_cost_detail_remain_money) == float(
                        #     student_cost_warning_remain_money)
                        # print float(student_cost_detail_remain_amount), float(
                        #     student_cost_warning_remain_amount), float(
                        #     student_cost_detail_remain_amount) == float(student_cost_warning_remain_amount)
                        if float(amount) == float(student_cost_detail_consume_amount) and float(
                                student_cost_consume_money) == float(student_cost_detail_consume_money) \
                                and float(student_cost_remain_money) == float(
                            student_cost_detail_remain_money) == float(
                            student_cost_warning_remain_money) \
                                and float(student_cost_detail_remain_amount) == float(
                            student_cost_warning_remain_amount):
                            return float(student_cost_detail_all_amount), float(amount), float(
                                student_cost_consume_money), \
                                   float(student_cost_detail_remain_amount), float(student_cost_remain_money),

    return False
