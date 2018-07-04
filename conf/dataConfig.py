# coding=utf8
# 配置文件
base_url = "https://demo.xiaogj.com"
result_file = "../report/testResult.txt"
fail_file = "../report/failResult.txt"
# 所有执行的PY文件目录
testcase_file = "../report/testcaseFile.txt"
# 综合结果后的输出
final_file = "../report/finalFile.txt"
# 所有执行的PY文件目录
all_execute_file = "../excute"
# 生产环境

# 异常日志文件，方便查询失败问题
fail_log = "..//report//logger.txt"

environment = "校管家release环境"
js_version = "04171646"
campus_id = "ee0b9bd9-6fdc-4184-b31d-42a2a49867ee"
email_info = {
    "smtp_server": "smtp.qq.com",
    "username": "2837657131@qq.com",
    "password": "jw123456",
    "sender": "smtp.qq.com",
    "receiver": ["258048759@qq.com", ]
}


class BugLevel(object):
    slight = "-轻微-"
    normal = "-一般-"
    critical = "-严重-"


class MySQLInFo(object):
    MYSQLHOST = "127.0.0.1"
    USER = "root"
    MYSQLPORT = 3306
    PASSWORD = "root"
    DATABASE = "test"
