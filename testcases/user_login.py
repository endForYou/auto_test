# -*- coding: utf-8 -*-
import unittest
from lib import xgjUser, util


class TestLogin(unittest.TestCase):
    # setUp用于初始化工作
    def setUp(self):
        pass

    def test_wrong_login(self):
        # 从用户池获取所需要的用户
        user = xgjUser.XgjUser()
        wrong_user_list = util.load_csv_file("wrong_account.csv")
        flag = True
        for user_record in wrong_user_list:
            wrong_login = user.login(user_record['username'], user_record['pwd'])
            if wrong_login:
                flag = False
        self.assertTrue(flag)

    def tearDown(self):
        pass


# 整个测试过程集中在unittest的main()模块中，其默认执行以test开头的方法
if __name__ == "__main__":
    # 构造测试套件
    pass
