# -*- coding: utf-8 -*-
import unittest
from lib import xgjUser, util, xgjRequest
from lib.built_in import *
from api import arrange_lesson_request


class ArrangeLesson(unittest.TestCase):
    # setUp用于初始化工作
    def setUp(self):
        session = xgjUser.XgjUser().login('admin@release')
        self.normal_request = arrange_lesson_request.ArrangeLessonRequest(session)

    def test_add_new_lesson_and_delete(self):
        start_date = get_current_date()
        end_date = get_current_date()
        result = self.normal_request.arrange_normal_lesson(start_date, end_date)
        self.assertTrue(result)


    # def test_add_one2one_lesson_and_delete(self):
    #     pass
        # open_date = get_current_date()
        # result = self.month_unit_request.add_new_class(open_date=open_date)
        #
        # self.assertTrue(result)
        # month_unit_class_name = result[0]
        # month_unit_class_id = result[1]
        # delete_result = self.month_unit_request.delete(month_unit_class_id)
        # query_result = self.month_unit_request.query_class(month_unit_class_name, is_month_unit=1, finished=0,
        #                                                    class_online_filter=0,
        #                                                    shift_type=7)
        # self.assertTrue(delete_result and not query_result)

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
