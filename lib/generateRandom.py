#coding=utf8
from checkMysql import checkMysql
import random


def generateRandom(pre):
    #生成字符串
    randomNum = random.randint(0, 99999999)
    #print randomNum
    stringNum = str(randomNum)
    if len(stringNum) < 8:
        #不足8位，则前面补0
        lastString = pre + (8 - len(stringNum)) * "0" + stringNum
        #print lastString
        return lastString
    else:
        lastString = pre + str(randomNum)
        #print lastString
        return lastString


def generatorNoExistsUser(pre, conn):
    #随机生成手机号码后，通过查询数据库，看该号码（账号）是否存在，若不存在，则返回该手机号码；否则，继续随机生成
    while True:
        mobilePhone = generateRandom(pre)
        sql = "select count(*) from bd_account where account='%s'" % mobilePhone
        requiredData = checkMysql().select(conn, sql)
        if requiredData[0][0] == 0:
            return mobilePhone


def generatorEmail():
    #生成随机Email地址
    list_string = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    list_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_sign = ["@129.com", "@126.com", "@111.com", "@333.com", "@163.com", "@qq.com", "@xx.com"]
    requiredString = random.choice(list_string) + random.choice(list_string) + random.choice(
        list_string) + random.choice(list_num) + random.choice(list_num) + random.choice(list_num) + random.choice(
        list_sign)
    return requiredString


def generator_mobile():
    #生成随机的电话号码
    pre_num = ["13", "14", "15", "16", "17", "18", "19"]
    mobile = random.choice(pre_num) + str(random.randint(100000000, 999999999))
    return mobile




if __name__ == "__main__":
    pre = "196"
    print generator_mobile()