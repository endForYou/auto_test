# coding=utf8
import re
from HReConf import dataConfig
import os


def getAllInterfaceName(
        preString,
        dirPath=dataConfig.reqUrlTest.ALLEXECUTEFILE,
        interfaceFile=dataConfig.reqUrlTest.INTERFACEFILE):

    allFile = os.listdir(dirPath)
    for singleFile in allFile:
        patternString = preString + ".*py$"
        if re.match(patternString, singleFile):
            newSingleFile = singleFile.split(".")[0]
            with open(interfaceFile, "a+") as openFile:
                openFile.write("======" + newSingleFile + "======" + "\n")
            filePath = os.path.join(dirPath, singleFile)
            # 定义一个临时存放接口名称的列表，为了去重复
            interfaceList = []
            with open(filePath, "r") as fileOpen:
                dataList = fileOpen.readlines()
                for j in dataList:
                    if re.match("\s*interfaceName[^,].*", j):
                        j = j.strip()
                        matchPattern = re.search(
                            "[\"\'](?P<interfaceName>.*?)[\"\']", j)
                        if matchPattern:
                            interfaceName = matchPattern.group("interfaceName")
                            if interfaceName not in interfaceList:
                                interfaceList.append(interfaceName)
                                with open(interfaceFile, "a+") as openFile:
                                    openFile.write(
                                        newSingleFile + interfaceName + "\n")
                        else:
                            continue


if __name__ == "__main__":
    dirPath = "..//testcases"
    preString = "supplierAddMemberConfirmRealDo"
    getAllInterfaceName(preString, dirPath)
