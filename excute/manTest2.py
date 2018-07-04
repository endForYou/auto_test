# -*- coding: utf-8 -*-
import unittest
import json
import requests
from otherlib.HTMLTestRunner import HTMLTestRunner
import time

test_dir = "E:\\project\\python_project\\xgj_interface\\testcases"
test_report = "E:\\project\\python_project\\xgj_interface\\report"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = './' + now + 'test_result.html'

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="xxx接口测试报告",
                            description="测试用例执行情况：")
    # 运行测试
    runner.run(discover)
    fp.close()  # 关闭报告文件
