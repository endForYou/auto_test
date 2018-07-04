#coding=utf8
import time


def getYmd():
    timeString = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return timeString


def getYmdHMS():
    timeString = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return timeString


def getStartAndEndTime():
    start = time.time()
    timeStart = time.strftime('%Y-%m-%d', time.localtime(start))
    end = time.time() + 31536000
    timeEnd = time.strftime('%Y-%m-%d', time.localtime(end))
    return timeStart, timeEnd


def getStartAndEndTimeExtra():
    now = time.time()
    start = now - 86400
    timeStart = time.strftime('%Y-%m-%d', time.localtime(start))
    end = now
    timeEnd = time.strftime('%Y-%m-%d', time.localtime(end))
    return timeStart, timeEnd


if __name__ == "__main__":
    print getYmd()
    timeString = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print timeString
    dt = "2016-11-07 11:34:54"

    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    print timestamp
