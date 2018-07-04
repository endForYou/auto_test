# -*- coding: utf-8 -*-
import unittest
from lib import xgjUser, util, xgjRequest
from lib.built_in import *
from api import charge_request, student_request, class_request, course_request, report_request, arrange_lesson_request
from suite import work_flow


class Smoke(unittest.TestCase):
    # setUp用于初始化工作
    def setUp(self):
        session = xgjUser.XgjUser().login('admin@release')
        self.charge_request = charge_request.ChargeRequest(session)
        self.student_request = student_request.StudentRequest(session)
        self.class_request = class_request.ClassRequest(session)
        self.course_request = course_request.CourseRequest(session)
        self.report_request = report_request.ReportRequest(session)
        self.arrange_lesson_request = arrange_lesson_request.ArrangeLessonRequest(session)

    # '''
    # 测试新增学员收费、查看收据、报读班级、出班、入班、排课点名、验证课消
    # '''
    #
    # def test_smoke(self):
    #     money = {
    #         'price': 100,
    #         'unit': 1,
    #         'discount': 0.90,
    #         'amount': 1,
    #         'direct_reduce': 0,
    #         'total': 90
    #
    #     }
    #     # 收费
    #     result = work_flow.charge_new(money, course_request_obj=self.course_request,
    #                                   class_request_obj=self.class_request,
    #                                   charge_request_obj=self.charge_request, report_request_obj=self.report_request)
    #     student_name = result
    #     student_info = self.student_request.query_student(student_name)
    #     # 排课点名及报表查询
    #     per_duration = 0.2
    #     consume_remain = money['amount'] - per_duration
    #     result = work_flow.arrange_lesson_and_call_the_roll(student_info, self.class_request,
    #                                                         self.arrange_lesson_request,
    #                                                         self.report_request, per_duration=per_duration,
    #                                                         where_amount=">0",
    #                                                         where_money=">20")
    #     print result
    #
    #     money_remain = money['total'] / money['amount'] * consume_remain
    #     consume_money = money['total'] - money_remain
    #     self.assertTrue(money['amount'] == result[0] and per_duration == result[1] and consume_money == result[
    #         2] and consume_remain == result[3] and money_remain == result[4])

    '''
    测试续费
    '''

    def test_performance(self):
        response = self.report_request.query_sign_bill_performance_list()
        print response

    '''
    测试预存
    '''

    def test_prestore(self):
        pass

    '''
    测试扩科
    '''

    def test_expand(self):
        pass

    '''
    1、班级没有学员正常删除
    '''

    def test_cannot_delete_if_have_students(self):
        pass

    '''
    测试查询班级功能，通过参数组合来测试
    '''

    def test_query_class(self):
        pass

    def tearDown(self):
        pass


# 整个测试过程集中在unittest的main()模块中，其默认执行以test开头的方法
if __name__ == "__main__":
    # 构造测试套件
    unittest.main()
