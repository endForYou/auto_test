# coding=utf8
import datetime
import json
import random
import re
import string
import time
from compat import basestring, builtin_str, integer_types, str
from httprunner.exception import ParamsError
import re


def gen_random_string(str_len):
    """ generate random string with specified length
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))


def get_random_num(pre, num_len):
    end = ''.join(str(random.randint(0, 9)) for _ in range(num_len - 1))
    return str(pre) + end


def get_timestamp(str_len=13):
    """ get timestamp string, length can only between 0 and 16
    """
    if isinstance(str_len, integer_types) and 0 < str_len < 17:
        return builtin_str(time.time()).replace(".", "")[:str_len]

    raise ParamsError("timestamp length can only between 0 and 16.")


def get_current_date(fmt="%Y-%m-%d"):
    """ get current date, default format is %Y-%m-%d
    """
    return datetime.datetime.now().strftime(fmt)


def get_week_day(date_str):
    """
    根据日期返回周几
    :param date_str:
    :return:
    """
    week_day_dict = {
        0: u'星期一',
        1: u'星期二',
        2: u'星期三',
        3: u'星期四',
        4: u'星期五',
        5: u'星期六',
        6: u'星期天',
    }
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day = date.weekday()
    return week_day_dict[day]



