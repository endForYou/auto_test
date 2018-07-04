import datetime

__author__ = 'Administrator'
dic = {
    "beans": [],
    "abc": "",
    "abcd": 1
}
print dic.get('beans', "test")
print dic.get('abc', "test2")
print dic.get('abcd', "1223")


class abc(object):
    ABC = "11222"

def get_current_date(fmt="%Y-%m-%d"):
    """ get current date, default format is %Y-%m-%d
    """
    return datetime.datetime.now().strftime(fmt)
print get_current_date()
now = datetime.datetime.now().strftime("%Y-%m-%d")
print now
time1 = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
print time1
