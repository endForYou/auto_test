# coding=utf8
#!/usr/bin/env python
# coding:utf-8
import requests


def sendNotice(mobilePhone, message):
    try:
        url = 'http://61.145.229.29:9006/MWGate/wmgw.asmx/MongateSendSubmit'
        data = {
            "userId": "J02918",
            "password": "298982",
            "pszMsg": message,
            "pszMobis": mobilePhone,
            "iMobiCount": "1",
            "pszSubPort": "*"}
        response = requests.post(url, data=data)
        text = response.text.encode("utf8")
        print text
    except Exception as e:
        Result_Data = '发送信息时异常:' + str(e)
        print Result_Data


if __name__ == '__main__':
    mobile_num = "13510689423"
    mobile_msg = 'ssssssssss\naaaaaa\nbbbb'
    sendNotice(mobile_num, mobile_msg)
