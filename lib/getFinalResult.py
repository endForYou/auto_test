# coding=utf8
import re
from HReConf import dataConfig
import os
import time
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')


def getFinalResult(
        moduleFile=dataConfig.reqUrlTest.INTERFACEFILE,
        result=dataConfig.reqUrlTest.RESULTFILE,
        finalFile=dataConfig.reqUrlTest.FINALFILE,
        failFile=dataConfig.reqUrlTest.FAILFILE):

    parentList = []
    childList = []
    with open(moduleFile, "r") as parentFile:
        parentData = parentFile.readlines()
        for i in parentData:
            parentList.append(i.replace(" ", "").strip())

    # 解决IOError: [Errno 2] No such file or directory: '../xxxx/testResult.txt'
    try:
        with open(result, "r") as childFile:
            childData = childFile.readlines()
            for j in childData:
                childList.append(j.replace(" ", "").strip())
    except BaseException:
        print "RESULTFILE不存在...."

    indexList = []

    for parentList_i in range(len(parentList)):
        if re.search("======.*?======", parentList[parentList_i]):
            indexList.append(parentList_i)

    # 加上最后的index
    indexList.append(len(parentList))
    interfaceList = []

    for i in range(len(indexList) - 1):
        interfaceList.append(parentList[indexList[i]:indexList[i + 1]])

    for k in interfaceList:
        if len(k) == 1:
            with open(finalFile, "a+") as finalOpen:
                finalOpen.write(k[0] + "\n")
        else:
            subject = k[0]
            with open(finalFile, "a+") as finalOpen:
                finalOpen.write(
                    subject + "------------------------>[START]" + "\n")
            executeList = k[1:]
            # 定义failFlag标识，如果failFlag大于0，则表示整个py文件用例执行失败
            failFlag = 0

            for executeList_i in executeList:
                # 定义一个累计数，用于存储是否有匹配的数据
                calcNum = 0
                # 解决IOError: [Errno 2] No such file or directory: '../xxxx/testResult.txt'
                if childList == []:
                    failFlag = failFlag + 1
                    subPre = "[" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                 time.localtime(time.time())) + "]"
                    string = subPre + "<[FAIL]>" + "<---->返回结果为:未知"
                    with open(finalFile, "a+") as finalOpen:
                        finalOpen.write(executeList_i + string + "\n")
                else:

                    for childList_i in childList:
                        # 次步骤中两个replace解决接口名称含有括号会解析失败的问题
                        if re.search(
                            executeList_i.replace(
                                "(",
                                "\(").replace(
                                ")",
                                "\)") + "<\[",
                                childList_i):
                            if re.search("<\[FAIL\]>", childList_i):
                                failFlag = failFlag + 1
                            with open(finalFile, "a+") as finalOpen:
                                finalOpen.write(
                                    executeList_i +
                                    childList_i.replace(
                                        executeList_i,
                                        "") +
                                    "\n")
                        else:
                            calcNum = calcNum + 1

                    if calcNum == len(childList):
                        failFlag = failFlag + 1
                        subPre = "[" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                     time.localtime(time.time())) + "]"
                        string = subPre + "<[FAIL]>" + "<---->返回结果为:未知"
                        with open(finalFile, "a+") as finalOpen:
                            finalOpen.write(executeList_i + string + "\n")

            executeString = ""
            if failFlag > 0:
                executeString = "------------------------>[FAIL]"
            elif failFlag == 0:
                executeString = "------------------------>[PASS]"
            with open(finalFile, "a+") as finalOpen:
                finalOpen.write(subject + executeString + "\n\n")

    # 单独写入一个保存失败请求的日志中
    with open(finalFile) as finalOpen:
        allData = finalOpen.readlines()
        for allData_i in allData:
            if re.search("<\[FAIL\]>", allData_i):
                allData_i = allData_i.strip()
                with open(failFile, "a+") as failOpen:
                    failOpen.write(allData_i + "\n")


if __name__ == "__main__":
    getFinalResult()
