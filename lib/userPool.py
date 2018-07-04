# coding=utf8
__author__ = 'Administrator'
from HReConf.dataConfig import *
TEST_ENV = 0
DEV_ENV = 1
ONLINE_ENV = 2


class UserPool(object):
    def get_all_user(self):
        if DayHRe.ENV == DEV_ENV:
            # receptionist接单员 dispatcher派单员 已签好协议
            # receptionist_manager 接单管理员 dispatcher_manager 派单管理员 未签协议
            # company 企业 receptionist接单员 已签好协议
            # company_dispatcher 企业 receptionist_manager接单管理员 未签协议
            # forward_dispatcher 转派的派单方 forward_receptionist转派的接单方
            # receptionist与forward_dispatcher是同一个企业，forward_dispatcher与forward_receptionist签订协议
            return {"company": ["qiye", "b123456"],
                    "receptionist": ["18692273905", "b123456"],
                    "dispatcher": ["15874271110", "b123456"],
                    "receptionist_manager": ["supplier2", "b123456"],
                    "company_dispatcher": ["qiye2", "b123456"],
                    "dispatcher_manager": ["tzh", "b123456"],
                    "platform": ["lq2", "b123456"],
                    "forward_dispatcher": ["18692273905", "b123456"],
                    "forward_receptionist": ["15675152577", "b123456"]
                    }
        elif DayHRe.ENV == ONLINE_ENV:
            return {"company": ["qiye", "b123456"],
                    "receptionist": ["18975816286", "b123456"],
                    "dispatcher": ["13564338421", "b123456"],
                    "receptionist_manager": ["supplier2", "b123456"],
                    "company_dispatcher": ["lyc", "b123456"],
                    "dispatcher_manager": ["sp2", "b123456"],
                    "platform": ["dayhro", "b123456"],
                    "forward_dispatcher": ["18975816286", "b123456"],
                    "forward_receptionist": ["18692273905", "b123456"]
                    }
        else:
            return {"company": ["qiye", "b123456"],
                    "receptionist": ["18692273905", "b123456"],
                    "dispatcher": ["15874271110", "b123456"],
                    "receptionist_manager": ["supplier2", "b123456"],
                    "company_dispatcher": ["qiye2", "b123456"],
                    "dispatcher_manager": ["tzh", "b123456"],
                    "platform": ["lq2", "b123456"],
                    "forward_dispatcher": ["18692273905", "b123456"],
                    "forward_receptionist": ["15675152577", "b123456"]
                    }

    def get_company_user(self):
        # 默认是测试环境
        if DayHRe.ENV == DEV_ENV:
            return ["qiye", "b123456"]
        elif DayHRe.ENV == ONLINE_ENV:
            return ["qiye", "b123456"]
        else:
            return ["qiye", "b123456"]

    def get_supplier_receptionist(self):
        # 默认是测试环境
        if DayHRe.ENV == DEV_ENV:
            return ["15874271110", "b123456"]
        elif DayHRe.ENV == ONLINE_ENV:
            return ["18975816286", "b123456"]  # sp2
        else:
            return ["15874271110", "b123456"]

    def get_supplier_dispatcher(self):
       # 默认是测试环境
        if DayHRe.ENV == DEV_ENV:
            return ["supplier2", "b123456"]
        elif DayHRe.ENV == ONLINE_ENV:
            return ["supplier2", "b123456"]
        else:
            return ["supplier2", "b123456"]

    def get_supplier_manager(self):
        # 默认是测试环境
        if DayHRe.ENV == DEV_ENV:
            return ["supplier2", "b123456"]
        elif DayHRe.ENV == ONLINE_ENV:
            return ["supplier2", "b123456"]
        else:
            return ["supplier2", "b123456"]

    def get_platform_manager(self):
        # 默认是测试环境
        if DayHRe.ENV == DEV_ENV:
            return ["lq2", "b123456"]
        elif DayHRe.ENV == ONLINE_ENV:
            return ["lq2", "b123456"]
        else:
            return ["lq2", "b123456"]
