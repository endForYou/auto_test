# coding=utf8


import requests
import urllib3
import unittest
import json
from conf import dataConfig, urlConfig


class XgjUser(object):

    def __init__(self):
        urllib3.disable_warnings()

    def login(self, user_name, pwd='888888'):
        data = {
            'name': user_name,
            'pwd': pwd,
            'ssx': False
        }

        session = requests.Session()
        url = dataConfig.base_url + urlConfig.login
        response = session.post(url, verify=False, data=data)
        if response.status_code == 200:
            response_str = response.content
            response_json = json.loads(response_str)
            if response_json.get('ErrorCode') == 200 and response_json.get('ErrorMsg') == 'OK':
                return session
            else:
                return False
        else:

            return False

        # unittest.TestCase.assertTrue(response.get('ErrorCode') == 200)
        # unittest.TestCase.assertTrue(response.get('ErrorMsg') == 'OK')


if __name__ == "__main__":
    user = XgjUser()
    urllib3.disable_warnings()
    user.login("admin@release")
