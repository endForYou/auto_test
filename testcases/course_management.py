# -*- coding: utf-8 -*-
import unittest
from lib import xgjUser, util
from api import course_request


class CourseManagement(unittest.TestCase):
    # setUp用于初始化工作
    def setUp(self):
        session = xgjUser.XgjUser().login('admin@release')
        self.request = course_request.CourseRequest(session)

    # def test_add_normal_course(self):
    #     # 从用户池获取所需要的用户
    #     params_list = util.load_csv_file("normal_course_params.csv")
    #     for params_record in params_list:
    #         course_name, course_id = self.xgj_request.add_new_course( self.campus_id,
    #                                                                  params_record['Unit'],
    #                                                                  params_record['IsOneToOne'],
    #                                                                  params_record['IsByTerm'],
    #                                                                  params_record['IsDynamicConsume'],
    #                                                                  params_record['EnableSubject'],
    #                                                                  params_record['EnableShiftSpec'],
    #                                                                  params_record['Status'],
    #                                                                  params_record['MinutesToTimes'],
    #                                                                  )
    #         self.assertTrue(course_id)

    def test_add_month_unit_course(self):
        params_list = util.load_csv_file("month_unit_course_params.csv")
        for params_record in params_list:
            course_name, course_id = self.request.add_new_course(
                params_record['Unit'],
                params_record['IsOneToOne'],
                params_record['IsByTerm'],
                params_record['IsDynamicConsume'],
                params_record['EnableSubject'],
                params_record['EnableShiftSpec'],
                params_record['Status'],
                params_record['MinutesToTimes'])
            self.assertTrue(course_id)

    def tearDown(self):
        pass


# 整个测试过程集中在unittest的main()模块中，其默认执行以test开头的方法
if __name__ == "__main__":
    # 构造测试套件
    unittest.main()
