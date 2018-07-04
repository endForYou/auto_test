#coding=utf8
import re


def verifyResult(expectValue, result):
    if re.search(expectValue, result):
        return True
    else:
        return False

