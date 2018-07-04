# coding=utf8
from lib import verifyResult
from conf import dataConfig
import os
import time
import sys
import re

reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')


def output_and_write_log(
        interface_name,
        now_value,
        expect_value,
        log_flag=1,
        write_flag=1):
    # 删除原来已经存在的记录文件
    now_value = now_value.strip()
    t = verifyResult.verifyResult(expect_value, now_value)
    sub_pre = "[" + time.strftime('%Y-%m-%d_%H:%M:%S',
                                 time.localtime(time.time())) + "]"
    if log_flag:
        if t:
            print sub_pre, interface_name, "<[PASS]>", "<---->返回结果为:", now_value
        else:
            print sub_pre, interface_name, "<[FAIL]>", "<---->返回结果为:", now_value

    if write_flag:
        # 写入文件时，结果不需要太长，截取前200个字符就可以了
        now_value = now_value[:200]
        if t:
            write_string = sub_pre + interface_name + \
                          "<[PASS]>" + "<---->返回结果为:" + now_value + "\n"
            to_file = file(dataConfig.result_file, "a+")
            to_file.write(write_string)
            to_file.close()
        else:
            write_string = sub_pre + interface_name + \
                          "<[FAIL]>" + "<---->返回结果为:" + now_value + "\n"
            to_file = file(dataConfig.result_file, "a+")
            to_file.write(write_string)
            to_file.close()


def output_and_write_log_by_flag(interface_name, flag, log_flag=1, write_flag=1):
    sub_pre = "[" + time.strftime('%Y-%m-%d_%H:%M:%S',
                                 time.localtime(time.time())) + "]"
    if log_flag:
        if flag:
            print sub_pre, interface_name, "<[PASS]>", "<---->返回结果为:正常"
        else:
            print sub_pre, interface_name, "<[FAIL]>", "<---->返回结果为:异常"

    if write_flag:
        if flag:
            write_string = sub_pre + interface_name + \
                          "<[PASS]>" + "<---->返回结果为:正常" + "\n"
            to_file = file(dataConfig.result_file, "a+")
            to_file.write(write_string)
            to_file.close()
        else:
            write_string = sub_pre + interface_name + \
                          "<[FAIL]>" + "<---->返回结果为:异常" + "\n"
            to_file = file(dataConfig.result_file, "a+")
            to_file.write(write_string)
            to_file.close()


