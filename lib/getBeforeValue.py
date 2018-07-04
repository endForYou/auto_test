#coding=utf8
import re


def getBeforeValue(last, first, string):
    #
    requiredValue = ""
    try:
        reversedNike = last[::-1]
        reversedString = string[::-1]
        reversedRes = first[::-1]
        matchString = reversedNike + ".*?" + "(?P<value>\d+)\".*?" + reversedRes
        matchPattern = re.search(matchString, reversedString, re.M | re.DOTALL | re.I)
        value = matchPattern.group("value")
        requiredValue = value[::-1]
    except:
        pass
    return requiredValue


def getBeforeString(last, first, string):
    requiredValue = ""
    try:
        reversedNike = last[::-1]
        reversedString = string[::-1]
        reversedRes = first[::-1]
        matchString = reversedNike + ".*?" + "\"(?P<value>.*?)\":\"" + reversedRes
        matchPattern = re.search(matchString, reversedString, re.M | re.DOTALL | re.I)
        value = matchPattern.group("value")
        value = value.split("\"")[-1]
        requiredValue = value[::-1]
    except:
        pass
    return requiredValue

#".*?(?P<value>\d+)\".*?" + reversedRes

def getBeforeValueExtra(last, first, second, string):
    requiredValue = ""
    try:
        reversedLast = last[::-1]
        reversedString = string[::-1]
        reversedSecond = second[::-1]
        reversedRes = first[::-1]
        matchString = "[\"]" + reversedLast + "[\"].*?" + reversedSecond + "\",[\"]?(?P<value>\d+)[\"]?:\"" + reversedRes
        matchPattern = re.search(matchString, reversedString, re.M | re.DOTALL | re.I)
        value = matchPattern.group("value")
        requiredValue = value[::-1]
    except:
        pass

    return requiredValue


if __name__ == "__main__":
    last = "test19720081754"
    firstString = "dd"
    second = "corp_id"
    string = '{"result":"true","resultDesc":null,"statusCode":null,"beans":null,"ext":null,"pb":{"pageNo":"1","pageSize":"100","pageDataCount":"4","pageCount":"1"},"maps":[{"uuid":6100000016995209,"dd":300019710,"corp_id":37966,"nickname":"test1","email":null,"mobilephone":"19488991201","status":"已激活","rolename":"超级管理员"},{"uuid":6100000017129565,"dd":300019756,"corp_id":37966,"nickname":"test19781385766","email":"dwn608@333.com","mobilephone":"19816144817","status":"未激活","rolename":null},{"uuid":6100000017129588,"dd":300019758,"corp_id":37966,"nickname":"test19736535764","email":"jnf112@qq.com","mobilephone":"19862040968","status":"未激活","rolename":null},{"uuid":6100000017129630,"dd":300019759,"corp_id":37966,"nickname":"test19720081754","email":"eft557@111.com","mobilephone":"19720081754","status":"未激活","rolename":null}]}'
    print getBeforeValueExtra(last, firstString, second, string)
